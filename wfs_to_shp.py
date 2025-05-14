from owslib.wfs import WebFeatureService
import geopandas as gpd
from owslib.util import ServiceException

url = "https://  "
username = "  "
password = "  "

def wfs_to_shapefile(layer_name, output_path, timeout=300):
        # Conectar ao serviço WFS
        wfs = WebFeatureService(url, version='1.1.0', username=username, password=password, timeout=timeout)
        
        # Obter os dados da camada
        response = wfs.getfeature(typename=layer_name)
        
        # Ler os dados com GeoPandas
        gdf = gpd.read_file(response)
        
        # Salvar como shapefile
        output_file = "D:/hend/Demandas/alerts_icmbio"
        gdf.to_file(output_file)
        
        print(f"Shapefile criado em: {output_file}")
        return output_file

wfs_to_shapefile("alerts_icmbio", "D:/hend/Demandas", timeout=300)
