from typing import Optional
from pydantic import BaseModel, Field

class Book:
      id: int
      title: str
      author: str
      description: str
      rating: int
      published_date: int

      def __init__(self, id, title, author, description, rating, published_date):
            self.id = id
            self.title = title
            self.author = author
            self.description = description
            self.rating = rating
            self.published_date = published_date


class BookRequest(BaseModel):
      id: Optional[int] = Field(title='Id is not needed', default= None)
      title: str = Field(min_length = 3)
      author: str = Field(min_length=1)
      description: str = Field(min_length=1, max_length=100)
      rating: int = Field(gt = -1, lt = 6)
      published_date: int = Field(gt = 1999, lt=2024)


      class Config:
            json_schema_extra = {
                  'example' : {
                        'title' : 'A new Book',
                        'author' : 'Azeez Bammeke',
                        'description' : 'Coding Book',
                        'rating' : 5,
                        'published_date' : 2021
                  }
            }


           

    #   def __init__(self, id, title, author, description, rating):
    #         self.id = id
    #         self.title = title
    #         self.author = author
    #         self.description = description
    #         self.rating = rating
