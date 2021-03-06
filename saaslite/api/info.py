from pydantic import BaseModel, HttpUrl


class Result(BaseModel):
    __root__: list[dict]


DB_GET = {
    'response_model': Result,
    'description': 'Query a SQLite database',
}

CSV_GET = {
    'response_model': Result,
    'description': 'Query a CSV file',
}


class Upload(BaseModel):
    object_key: str
    upload_url: HttpUrl


UPLOAD_POST = {
    'response_model': Upload,
    'description': 'Creates a temporary upload URL to upload your own file',
}
