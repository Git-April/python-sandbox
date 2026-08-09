from datetime import datetime, timezone

from typing import Annotated, Literal, Any
from typing_extensions import NotRequired, TypedDict

from annotated_types import Gt

from pydantic_core.core_schema import ValidatorFunctionWrapHandler

from pydantic import BaseModel, PositiveInt, ValidationError, TypeAdapter, field_validator

class User(BaseModel):
  id: int
  name: str = 'John Doe'
  signup_ts: datetime | None
  tastes: dict[str, PositiveInt]

external_data = {
  'id': 123,
  'signup_ts': '2019-06-01 12:22',
  'tastes': {
    'wine': 9,
    b'cheese': 7,
    'cabbage': '1'
  },
}

user = User(**external_data)

print(user.id)
print(user.model_dump())

external_data2 = {'id': 'not_an_int', 'tastes': {}}

try:
  User(**external_data2)
except ValidationError as e:
  print(e.errors())

class Fruit(BaseModel):
  name: str
  color: Literal['red', 'green']
  weight: Annotated[float, Gt(0)]
  bazam: dict[str, list[tuple[int, bool, float]]]

print(
  Fruit(
    name='Apple',
    color='red',
    weight=4.2,
    bazam={'foobar': [(1, True, 0.1)]}
  )
)

class Meeting(BaseModel):
  when: datetime
  where: bytes
  why: str = 'No idea'

m = Meeting(when='2020-01-01T12:00', where='home')
print(m.model_dump(exclude_unset=True))
print(m.model_dump(exclude={'where'}, mode='json'))
print(m.model_dump_json(exclude_defaults=True))

class Address(BaseModel):
  street: str
  city: str
  zipcode: str

class Meeting2(BaseModel):
  when: datetime
  where: Address
  why: str = 'No idea'

print(Meeting2.model_json_schema())

m = Meeting.model_validate({'when': '2020-01-01T12:00', 'where': 'home'})
print(m)

try:
  m = Meeting.model_validate(
    {'when': '2020-01-01T12:00', 'where': 'home'}, strict=True
  )
except ValidationError as e:
  print(e)

m_json = Meeting.model_validate_json(
  '{"when": "2020-01-01T12:00", "where": "home"}'
)

print(m_json)

class Meeting3(TypedDict):
  when: datetime
  where: bytes
  why: NotRequired[str]

meeting_adapter = TypeAdapter(Meeting3)
m = meeting_adapter.validate_python(
  {'when': '2020-01-01T12:00', 'where': 'home'}
)
print(m)
meeting_adapter.dump_python(m, exclude={'where'})

print(meeting_adapter.json_schema())

class Meeting4(BaseModel):
  when: datetime

  @field_validator('when', mode='wrap')
  def when_now(
    cls, input_value: Any, handler: ValidatorFunctionWrapHandler
  ) -> datetime:
    if input_value == 'now':
      return datetime.now()
    when = handler(input_value)
    if when.tzinfo is None:
      when = when.replace(tzinfo=timezone.utc)
    return when

print(Meeting4(when='2020-01-01T12:00+01:00'))
print(Meeting4(when='now'))
print(Meeting4(when='2020-01-01T12:00'))