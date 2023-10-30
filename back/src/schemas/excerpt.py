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


class ExcerptLog(ExcerptCreate):
    preprocessed_text: str
    category: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "text": "El movimiento moderno de estudios jurídicos empíricos tiene antecedentes bien conocidos en las tradiciones de derecho y sociedad y derecho y economía de la segunda mitad del siglo XX. Menos conocido es el conjunto de investigaciones empíricas sobre fenómenos jurídicos del período anterior a la Segunda Guerra Mundial. Este artículo es un extenso ensayo bibliográfico que examina la investigación jurídica empírica en lengua inglesa desde aproximadamente 1940 y antes. El artículo se organiza en torno a los temas de la investigación: justicia penal, justicia civil (estudios generales de litigios civiles, litigios e indemnizaciones por accidentes de automóvil, divorcio, demandas de menor cuantía, jurisdicción y procedimiento, jurados civiles), deuda y quiebra, banca, tribunales de apelación, necesidades jurídicas, profesión jurídica (incluida la educación jurídica), y dotación y selección de personal judicial. Acompaña al artículo una extensa bibliografía de artículos de investigación, libros e informes.",
                    "preprocessed_text": "movimient modern estudi jurid empir antecedent bien conoc tradicion derech socied derech economi segund mit sigl xx men conoc conjunt investig empir fenomen jurid period anterior segund guerr mundial articul extens ensay bibliograf examin investig jurid empir lengu ingles aproxim mil novecientos cuarent articul organiz torn tem investig justici penal justici civil estudi general litigi civil litigi indemniz accident automovil divorci demand menor cuanti jurisdiccion proced jur civil deud quiebr banc tribunal apel neces jurid profesion jurid inclu educ jurid dotacion seleccion personal judicial acompan articul extens bibliografi articul investig libr inform",
                    "category": 16
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
