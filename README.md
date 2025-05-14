# WFS to Shapefile Exporter

Este script Python permite acessar uma camada de um serviço WFS protegido por autenticação e exportá-la como um arquivo Shapefile, utilizando as bibliotecas `OWSLib` e `GeoPandas`. É útil para integrar dados geoespaciais de servidores WFS com fluxos de trabalho em ambientes GIS como o **ArcGIS Pro**.

## 📦 Requisitos

Instale as dependências com:

```bash
pip install owslib geopandas
```

> ⚠️ É necessário ter o **GDAL** corretamente configurado para salvar arquivos Shapefile com o GeoPandas.

## 🚀 Como usar

```python
wfs_to_shapefile("alerts_icmbio", "C:/sua/pastas", timeout=300)
```

## ⚙️ Parâmetros da função

| Parâmetro     | Descrição                                                            |
| ------------- | -------------------------------------------------------------------- |
| `layer_name`  | Nome da camada a ser baixada do serviço WFS                          |
| `output_path` | Caminho do diretório onde o Shapefile será salvo                     |
| `timeout`     | Tempo máximo (em segundos) para a resposta do servidor (padrão: 300) |


## 🧠 Observações

O caminho de saída está fixo no código como:

```python
output_file = "D:/hend/Demandas/alerts_icmbio"
```

Para torná-lo dinâmico, substitua por:

```python
output_file = f"{output_path}/{layer_name}.shp"
