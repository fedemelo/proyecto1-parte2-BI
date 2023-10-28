from pydantic import BaseModel


class ExcerptCreate(BaseModel):
    text: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "text": "La investigación de homicidios es una de las tareas más prestigiosas y difíciles de los cuerpos de seguridad modernos. La mayoría de los departamentos de policía metropolitanos..."
                },
                {
                    "text": "El capítulo examina la contribución que la teoría de las Relaciones Internacionales ha hecho a la lectura y práctica de la construcción de paz."
                }
            ]
        }
    }


class ExcerptResponse(ExcerptCreate):
    id: str
    category: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "888f2fd5-a0ca-4a03-9f49-af9e37e80885",
                    "text": "La investigación de homicidios es una de las tareas más prestigiosas y difíciles de los cuerpos de seguridad modernos. La mayoría de los departamentos de policía metropolitanos...",
                    "category": 16
                }
            ]
        }
    }
