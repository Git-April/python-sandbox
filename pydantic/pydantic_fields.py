from typing import Annotated, Union, Literal
from warnings import deprecated
import warnings
from uuid import uuid4
from decimal import Decimal

from typing_extensions import Self

from pydantic import BaseModel, Field, WithJsonSchema, EmailStr, ValidationError, ConfigDict, Discriminator, Tag, model_validator, computed_field
from pydantic.dataclasses import dataclass

class Model(BaseModel):
  name: str = Field(frozen=True)

class Model(BaseModel):
  name: Annotated[str, Field(strict=True), WithJsonSchema({'extra': 'data'})]

class Model(BaseModel):
  int_list: list[Annotated[int, Field(gt=0)]]

class Model(BaseModel):
  field_ok: Annotated[int | None, Field(deprecated=True)] = None

class Model(BaseModel):
  a: Annotated[
    int, Field(gt=1), WithJsonSchema({'extra': 'data'}), Field(alias='b')
  ] = 1

field_info = Model.model_fields['a']
print(field_info.annotation)
print(field_info.alias)
print(field_info.metadata)

class User(BaseModel):
  name: str = 'John Doe'
  age: int = Field(default=20)

class User(BaseModel):
  id: str = Field(default_factory=lambda: uuid4().hex)

class User(BaseModel):
  email: EmailStr
  username: str = Field(default_factory=lambda data: data['email'])

user = User(email='user@example.com')
print(user.username)

class User(BaseModel):
  age: int = Field(default='twelve', validate_default=True)

try:
  user = User()
except ValidationError as e:
  print(e)

class Model(BaseModel):
  item_counts: list[dict[str, int]] = [{}]

m1 = Model()
m1.item_counts[0]['a'] = 1
print(m1.item_counts)

m2 = Model()
print(m2.item_counts)

class User(BaseModel):
  name: str = Field(alias='username')

user = User(username='johndoe')
print(user)
print(user.model_dump(by_alias=True))

class User(BaseModel):
  name: str = Field(validation_alias='username')

user = User(username='johndoe')
print(user)
print(user.model_dump(by_alias=True))

class User(BaseModel):
  name: str = Field(serialization_alias='username')

user = User(name='johndoe')
print(user)
print(user.model_dump(by_alias=True))

class User(BaseModel):
  name: str = Field(alias='username')

user = User(username='johndoe')

class User(BaseModel):
  model_config = ConfigDict(validate_by_name=True)

  name: str = Field(alias='username')

user = User(name='johndoe')


class User(BaseModel):
  model_config = ConfigDict(validate_by_name=True)

  name: Annotated[str, Field(alias='username')]

user = User(name='johndoe')

class User(BaseModel):
  model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

  name: str = Field(alias='username')

user = User(name='johndoe')
user = User(username='johndoe')

class MyModel(BaseModel):
  my_field: int = Field(
    alias='myValidationAlias',
    serialization_alias='my_field'
  )

m = MyModel(myValidationAlias=1)
print(m.model_dump(by_alias=True))

class Model(BaseModel):
  positive: int = Field(gt=0)
  short_str: str = Field(max_length=3)
  precise_decimal: Decimal = Field(max_digits=5, decimal_places=2)

class Model(BaseModel):
  positive: Union[int, None] = Field(gt=0)
  negative: Annotated[Union[int, None], Field(lt=0)]

class User(BaseModel):
  name: str = Field(strict=True)
  age: int = Field(strict=False)

user = User(name='John', age='42')
print(user)

@dataclass
class Foo:
  bar: str
  baz: str = Field(init_var=True)
  qux: str = Field(kw_only=True)

class Model(BaseModel):
  foo: Foo

model = Model(foo=Foo('bar', baz='baz', qux='qux'))
print(model.model_dump())

class User(BaseModel):
  name: str = Field(repr=True)
  age: int = Field(repr=False)

user = User(name='John', age=42)
print(user)

class Cat(BaseModel):
  pet_type: Literal['cat']
  age: int

class Dog(BaseModel):
  pet_type: Literal['dog']
  age: int

class Model(BaseModel):
  pet: Union[Cat, Dog] = Field(discriminator='pet_type')

print(Model.model_validate({'pet': {'pet_type': 'cat', 'age': 12}}))

class Cat(BaseModel):
  pet_type: Literal['cat']
  age: int

class Dog(BaseModel):
  pet_kind: Literal['dog']
  age: int

def pet_discriminator(v):
  if isinstance(v, dict):
    return v.get('pet_type', v.get('pet_kind'))
  return getattr(v, 'pet_type', getattr(v, 'pet_kind', None))

class Model(BaseModel):
  pet: Union[Annotated[Cat, Tag('cat')], Annotated[Dog, Tag('dog')]] = Field(
    discriminator=Discriminator(pet_discriminator)
  )

print(repr(Model.model_validate({'pet': {'pet_type': 'cat', 'age': 12}})))
print(repr(Model.model_validate({'pet': {'pet_kind': 'dog', 'age': 12}})))

class User(BaseModel):
  name: str = Field(frozen=True)
  age: int

user = User(name='John', age=42)

try:
  user.name = 'Jane'
except ValidationError as e:
  print(e)

class User(BaseModel):
  name: str
  age: int = Field(exclude=True)

user = User(name='John', age=42)
print(user.model_dump())

class Model(BaseModel):
  deprecated_field: Annotated[int, Field(deprecated='This is deprecated')]

print(Model.model_json_schema()['properties']['deprecated_field'])

class Model(BaseModel):
  deprecated_field: Annotated[int, Field(deprecated='This is deprecated')]

  alt_form: Annotated[int, Field(deprecated=deprecated('This is deprecated'))]

class Model(BaseModel):
  deprecated_field: Annotated[int, Field(deprecated=True)]

print(Model.model_json_schema()['properties']['deprecated_field'])

class Model(BaseModel):
  deprecated_field: int = Field(deprecated='This is deprecated')

  @model_validator(mode='after')
  def validate_model(self) -> Self:
    with warnings.catch_warnings():
      warnings.simplefilter('ignore', DeprecationWarning)
      self.deprecated_field = self.deprecated_field * 2

class Box(BaseModel):
  width: float
  height: float
  depth: float

  @computed_field
  @property
  def volume(self) -> float:
    return self.width * self.height * self.depth

print(Box.model_json_schema(mode='serialization'))

b = Box(width=1, height=2, depth=3)
print(b.model_dump())

class Box(BaseModel):
  width: float
  height: float
  depth: float

  @computed_field
  @property
  @deprecated("'volume' is deprecated")
  def volume(self) -> float:
    return self.width * self.height * self.depth