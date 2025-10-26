from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import sys
def analizar_secuencia(ruta_archivo_fasta):
    """
    Función principal que orquesta el análisis de la secuencia.
    Recibe la ruta al archivo FASTA y muestra los resultados.
    """
    try:
        record_secuencia = SeqIO.read(ruta_archivo_fasta, "fasta")
        secuencia_adn = record_secuencia.seq
        caracteres_validos = "ATCGN"
        if not all(nucleotido.upper() in caracteres_validos for nucleotido in secuencia_adn):
            print("Error: El archivo no parece contener una secuencia de ADN válida.")
            return
        longitud = len(secuencia_adn)
        contenido_gc = gc_fraction(secuencia_adn) * 100
        secuencia_proteina = secuencia_adn.translate()
        print("\n" + "="*50)
        print(f"ANÁLISIS DE LA SECUENCIA: {record_secuencia.id}")
        print("="*50 + "\n")
        print(f"Longitud de la secuencia de ADN: {longitud} pb")
        print(f"Contenido GC: {contenido_gc:.2f} %")
        print("\n" + "-"*50 + "\n")
        print(" TRANSLACIÓN A PROTEÍNA ".center(50, "*"))
        print(f"\n{secuencia_proteina}\n")
        print("="*50)
    except FileNotFoundError:
        print(f"\nError: No se pudo encontrar el archivo en la ruta: '{ruta_archivo_fasta}'")
        print("Asegúrate de que el nombre del archivo esté bien escrito y en la carpeta correcta.\n")
    except ValueError:
        print(f"\nError: El archivo '{ruta_archivo_fasta}' está vacío o contiene más de una secuencia.")
        print("Este script está diseñado para analizar un archivo FASTA con una única secuencia.\n")
    except Exception as e:
        print(f"\nHa ocurrido un error inesperado: {e}\n")
if __name__ == "__main__":
    if len(sys.argv) > 1:
        nombre_archivo = sys.argv[1]
        print(f"\nIniciando análisis para el archivo proporcionado: {nombre_archivo}...")
    else:
        nombre_archivo = "secuencia_ejemplo.fasta"
        print(f"\nNo se especificó un archivo. Usando el archivo por defecto: '{nombre_archivo}'...")
    analizar_secuencia(nombre_archivo)
