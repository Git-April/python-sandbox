import abc
from random import randint
import inspect

import logging
from datetime import datetime
from typing import Optional, Any, Annotated, Generic, TypeVar, Self, ClassVar
from sqlalchemy import ARRAY, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from pydantic import BaseModel, ConfigDict, PydanticUserError, ValidationError, StringConstraints, model_validator, SerializeAsAny, create_model, Field, PrivateAttr, field_validator, RootModel

class User(BaseModel):
  id: int
  name: str = 'Jane Doe'

  model_config = ConfigDict(str_max_length=18)

user = User(id='123')

assert user.name == 'Jane Doe'
assert user.id == 123
assert isinstance(user.id, int)

assert user.model_dump() == {'id': 123, 'name': 'Jane Doe'}

user.id = 321
assert user.id == 321

class Boo(BaseModel):
  int_: Optional[int] = None

m = Boo(int_=123)

class Model(BaseModel):
  a: int
  b: float
  c: str

print(Model(a=3.000, b='2.72', c=b'binary data').model_dump())

class Model(BaseModel):
  items: list[int]

print(Model(items=(1, 2, 3)))

class Model(BaseModel):
  x: int

  model_config = ConfigDict(extra='allow')

m = Model(x=1, y='a')
assert m.model_dump() == {'x': 1, 'y': 'a'}
assert m.__pydantic_extra__ == {'y': 'a'}

class Foo(BaseModel):
  count: int
  size: Optional[float] = None

class Bar(BaseModel):
  apple: str = 'x'
  banana: str = 'y'

class Spam(BaseModel):
  foo: Foo
  bars: list[Bar]

m = Spam(foo={'count': 4}, bars=[{'apple': 'x1'}, {'apple': 'x2'}])
print(m)

class Foo2(BaseModel):
  x: 'Bar2'

try:
  Foo2.model_json_schema()
except PydanticUserError as e:
  print(e)

class Bar2(BaseModel):
  pass

Foo2.model_rebuild()
print(Foo2.model_json_schema())

class User(BaseModel):
  id: int
  name: str = 'John Doe'
  signup_ts: Optional[datetime] = None

m = User.model_validate({'id': 123, 'name': 'James'})
print(m)

try:
  m = User.model_validate_json({'id': 123, 'name': '123'})
except ValidationError as e:
  print(e)

m = User.model_validate_strings({'id': '123', 'name': 'James'})
print(m)

m = User.model_validate_strings(
  {'id': '123', 'name': 'James', 'signup_ts': '2024-04-01T12:00:00'}
)
print(m)

try:
  m = User.model_validate_strings(
    {'id': '123', 'name': 'James', 'signup_ts': '2024-04-01'}, strict=True
  )
except ValidationError as e:
  print(e)

class MyModel(BaseModel):
  id: int

  def model_post_init(self, context: Any) -> None:
    logging.info(f"Model initialized with id %d", self.id)

class Model(BaseModel):
  list_of_ints: list[int]
  a_float: float

data = {
  'list_of_ints': ['1', 2, 'bad'],
  'a_float': 'not a float'
}

try:
  Model(**data)
except ValidationError as e:
  print(e)

class Base(DeclarativeBase):
  pass

class CompanyOrm(Base):
  __tablename__ = 'companies'

  id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
  public_key: Mapped[str] = mapped_column(
    String(20), index=True, nullable=False, unique=True
  )
  domains: Mapped[list[str]] = mapped_column(ARRAY(String(255)))

class CompanyModel(BaseModel):
  model_config = ConfigDict(from_attributes=True)

  id: int
  public_key: Annotated[str, StringConstraints(max_length=20)]
  domains: list[Annotated[str, StringConstraints(max_length=255)]]

co_orm = CompanyOrm(
  id=123,
  public_key='foobar',
  domains= ['example.com', 'foobar.com'],
)
print(co_orm)
co_model = CompanyModel.model_validate(co_orm)
print(co_model)

class PetCls:
  def __init__(self, *, name: str) -> None:
    self.name = name

class PersonCls:
  def __init__(self, *, name: str, pets: list[PetCls]) -> None:
    self.name = name
    self.pets = pets

class Pet(BaseModel):
  model_config = ConfigDict(from_attributes=True)

  name: str

class Person(BaseModel):
  model_config = ConfigDict(from_attributes=True)

  name: str
  pets: list[Pet]

bones = PetCls(name='Bones')
orion = PetCls(name='Orion')
anna = PersonCls(name='Anna', pets=[bones, orion])
anna_model = Person.model_validate(anna)
print(anna_model)

class BarModel(BaseModel):
  whatever: int

class FooBarModel(BaseModel):
  banana: float
  foo: str
  bar: BarModel

m = FooBarModel(banana=3.14, foo='hello', bar={'whatever': 123})

print(m.model_copy(update={'banana': 0}))
print(id(m.bar) == id(m.model_copy().bar))
print(id(m.bar) == id(m.model_copy(deep=True).bar))

class DataModel(BaseModel):
  number: int

class Response[DataT](BaseModel):
  data: DataT

print(Response[int](data=1))
print(Response[str](data='value'))
print(Response[str](data='value').model_dump())

data = DataModel(number=1)
print(Response[DataModel](data=data).model_dump())
try:
  Response[int](data='value')
except ValidationError as e:
  print(e)

TypeX = TypeVar('TypeX')

class BaseClass(BaseModel, Generic[TypeX]):
  X: TypeX

class ChildClass(BaseClass[TypeX], Generic[TypeX]):
  pass

print(ChildClass[int](X=1))

TypeY = TypeVar('TypeY')
TypeZ = TypeVar('TypeX')

class BaseClass(BaseModel, Generic[TypeX, TypeY]):
  x: TypeX
  y: TypeY

class ChildClass(BaseClass[int, TypeY], Generic[TypeY, TypeZ]):
  z: TypeZ

print(ChildClass[str, int](x='1', y='y', z='3'))

DataT = TypeVar('DataT')

class Response(BaseModel, Generic[DataT]):
  data: DataT

  @classmethod
  def model_parametrized_name(cls, params: tuple[type[Any], ...]) -> str:
    return f'{params[0].__name__.title()}Response'

print(repr(Response[int](data=1)))
print(repr(Response[str](data='a')))

T = TypeVar('T')

class ResponseModel(BaseModel, Generic[T]):
  content: T

class Product(BaseModel):
  name: str
  price: float

class Order(BaseModel):
  id: int
  product: ResponseModel[Product]

product = Product(name='Apple', price=0.5)
response = ResponseModel[Product](content=product)
order = Order(id=1, product=response)
print(repr(order))

class InnerT(BaseModel, Generic[T]):
  inner: T

class OuterT(BaseModel, Generic[T]):
  outer: T
  nested: InnerT[T]

nested = InnerT[int](inner=1)
print(OuterT[int](outer=1, nested=nested))

try:
  print(OuterT[int](outer='a', nested=InnerT(inner='a')))
except ValidationError as e:
  print(e)

class GenericModel(BaseModel, Generic[T]):
  a: T

class Model(BaseModel):
  inner: GenericModel[Any]

print(repr(Model.model_validate(Model(inner=GenericModel[int](a=1)))))

class GenericModel(BaseModel, Generic[T]):
  a: T

  @model_validator(mode='after')
  def validate_after(self: Self) -> Self:
    print('after validator running custom validation...')
    return self

class Model(BaseModel):
  inner: GenericModel[Any]

m = Model.model_validate(Model(inner=GenericModel[int](a=1)))
print(repr(m))

T = TypeVar('T')
U = TypeVar('U', bound=int)
V = TypeVar('V', default=str)

class Model(BaseModel, Generic[T, U, V]):
  t: T
  u: U
  v: V

print(Model(t='t', u=1, v='v'))

try:
  Model(t='t', u='u', v=1)
except ValidationError as e:
  print(e)

ItemT = TypeVar('ItemT', bound='ItemBase')

class ItemBase(BaseModel): ...

class IntItem(ItemBase):
  value: int

class ItemHolder(BaseModel, Generic[ItemT]):
  item: ItemT

loaded_data = {'item': {'value': 1}}

print(ItemHolder(**loaded_data))

print(ItemHolder[IntItem](**loaded_data))

class ErrorDetails(BaseModel):
  foo: str

ErrorDataT = TypeVar('ErrorDataT', bound=ErrorDetails)

class Error(BaseModel, Generic[ErrorDataT]):
  message: str
  details: ErrorDataT

class MyErrorDetails(ErrorDetails):
  bar: str

error = Error(
  message='We just had an error',
  details=MyErrorDetails(foo='var', bar='var2'),
)
assert error.model_dump() == {
  'message': 'We just had an error',
  'details': {
    'foo': 'var',
    'bar': 'var2'
  },
}

error = Error[ErrorDetails](
  message='We just had an error',
  details=ErrorDetails(foo='var'),
)
assert error.model_dump() == {
  'message': 'We just had an error',
  'details': {
    'foo': 'var',
  },
}

TBound = TypeVar('TBound', bound=BaseModel)
TNoBound = TypeVar('TNoBound')

class IntValue(BaseModel):
  value: int

class ItemBound(BaseModel, Generic[TBound]):
  item: TBound

class ItemNoBound(BaseModel, Generic[TNoBound]):
  item: TNoBound

item_bound_inferred = ItemBound(item=IntValue(value=3))
item_bound_explicit = ItemBound[IntValue](item=IntValue(value=3))
item_no_bound_inferred = ItemNoBound(item=IntValue(value=3))
item_no_bound_explicit = ItemNoBound[IntValue](item=IntValue(value=3))

class ErrorDetails(BaseModel):
  foo: str

ErrorDataType = TypeVar('ErrorDataType', default=ErrorDetails)

class Error(BaseModel, Generic[ErrorDataType]):
  message: str
  details: ErrorDataType

class MyErrorDetails(ErrorDetails):
  bar: str

error = Error(
  message='We just had an error',
  details=MyErrorDetails(foo='var', bar='baz')
)
assert error.model_dump() == {
  'message':'We just had an error',
  'details':{
    'foo': 'var',
  },
}

class SerializeAsAnyError(BaseModel, Generic[ErrorDataType]):
  message: str
  details: SerializeAsAny[ErrorDataType]

error = SerializeAsAnyError(
  message='We just had an error',
  details=MyErrorDetails(foo='var', bar='baz')
)
assert error.model_dump() == {
  'message':'We just had an error',
  'details':{
    'foo': 'var',
    'bar': 'baz',
  },
}

DynamicFoobarModel = create_model('DynamicFoobarModel', foo = str, bar=(int, 123))

class StaticFoobarModel(BaseModel):
  foo: str
  bar: int = 123

DynamicModel = create_model(
  'DynamicModel',
  foo=(str, Field(alias='FOO')),
  bar=Annotated[str, Field(description='Bar field')],
  _private=(int, PrivateAttr(default=1))
)

class FooModel(BaseModel):
  foo: str
  bar: int = 123

BarModel = create_model(
  'BarModel',
  apple=(str, 'russet'),
  banana=(str, 'yellow'),
  __base__=FooModel,
)
print(BarModel)
print(BarModel.model_fields.keys())

def alphanum(cls, v):
  assert v.isalnum(), 'must be alphanumeric'
  return v

validators = {
  'username_validator': field_validator('username')(alphanum)
}

UserModel = create_model(
  'UserModel', username=(str, ...), __validators__=validators
)

user = UserModel(username='scolvin')
print(user)

try:
  UserModel(username='scolvi%n')
except ValidationError as e:
  print(e)

Pets = RootModel[list[str]]
PetsByName = RootModel[dict[str, str]]

print(Pets(['dog', 'cat']))
print(Pets(['dog', 'cat']).model_dump_json())
print(Pets.model_validate(['dog', 'cat']))
print(Pets.model_json_schema())

print(PetsByName({'Otis': 'dog', 'Milo': 'cat'}))
print(PetsByName({'Otis': 'dog', 'Milo': 'cat'}).model_dump_json())
print(PetsByName.model_validate({'Otis': 'dog', 'Milo': 'cat'}))

class Pets(RootModel):
  root: list[str]

  def __iter__(self):
    return iter(self.root)

  def __getitem__(self, item):
    return self.root[item]

pets = Pets.model_validate(['dog', 'cat'])
print(pets[0])
print([pet for pet in pets])

class Pets(RootModel[list[str]]):
  def describe(self) -> str:
    return f'Pets: {", ".join(self.root)}'

my_pets = Pets.model_validate(['dog', 'cat'])
print(my_pets.describe())

class FooBarModel(BaseModel):
  model_config = ConfigDict(frozen=True)

  a: str
  b: dict

foobar = FooBarModel(a='hello', b={'apple': 'pear'})

try:
  foobar.a = 'different'
except ValidationError as e:
  print(e)

print(foobar.a)
print(foobar.b)
foobar.b['apple'] = 'grape'
print(foobar.b)

class FooBarModel(BaseModel, abc.ABC):
  a: str
  b: int

  @abc.abstractmethod
  def my_abstract_method(self):
    pass

class Model(BaseModel):
  a: int
  b: int = 2
  c: int = 1
  d: int = 0
  e: float

print(Model.model_fields.keys())
m = Model(e=2, a=1)
print(m.model_dump())
try:
  Model(a='x', b='x', c='x', d='x', e='x')
except ValidationError as err:
  error_locations = [e['loc'] for e in err.errors()]

print(error_locations)

class Model(BaseModel):
  x: ClassVar[int] = 1

  y: int = 2

m = Model()
print(m)
print(Model.x)

class TimeAwareModel(BaseModel):
  _processed_at: datetime = PrivateAttr(default_factory=datetime.now)
  _secret_value: str

  def model_post_init(self, context: Any) -> None:
    self._secret_value = randint(1, 5)

m = TimeAwareModel()
print(m._processed_at)
print(m._secret_value)

class FooModel(BaseModel):
  id: int
  name: str
  description: str = 'Foo'
  apple: int = Field(alias='pear')

print(inspect.signature(FooModel))

class MyModel(BaseModel):
  id: int
  info: str = 'Foo'

  def __init__(self, id: int = 1, *, bar: str, **data) -> None:
    """My custom init!"""
    super().__init__(id=id, bar=bar, **data)

print(inspect.signature(MyModel))

class Pet(BaseModel):
  name: str
  species: str

a = Pet(name='Bones', species='dog')

match a:
  case Pet(species='dog', name=dog_name):
    print(f'{dog_name} is a dog')
  case _:
    print('No dog matched')

class C1:
  arr = []

  def __init__(self, in_arr):
    self.arr = in_arr

class C2(BaseModel):
  arr: list[int]

arr_orig = [1, 9, 10, 3]

c1 = C1(arr_orig)
c2 = C2(arr=arr_orig)
print(f'{id(c1.arr) == id(c2.arr)=}')