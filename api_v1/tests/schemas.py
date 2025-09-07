from pydantic import BaseModel, ConfigDict

class TestsBase(BaseModel):
    type_of_tests:str
    date:str
    results: float
    
class TestCreate(TestsBase):
    pass 

class TestUpdate(TestCreate):
    pass

class TestUpdatePartial(TestCreate):
    type_of_tests:str | None = None
    date:str | None = None
    results: float | None = None
        
    
class Tests(TestsBase):
    model_config = ConfigDict(from_attributes=True)
    id: int