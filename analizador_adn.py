import sys
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
from Bio.Data.CodonTable import TranslationError

def calcular_gc(secuencia):
    if not secuencia:
        return 0.0
    return gc_fraction(secuencia) * 100

def traducir_a_proteina(secuencia):
    return secuencia.translate()

def analizar_archivo_fasta(ruta_entrada, ruta_salida):
    print(f"Procesando archivo de entrada: '{ruta_entrada}'...")
    
    try:
        with open(ruta_salida, 'w') as archivo_salida:
            registros = SeqIO.parse(ruta_entrada, "fasta")
            
            num_secuencias_procesadas = 0
            num_secuencias_con_error = 0
            
            for record in registros:
                id_secuencia = record.id
                secuencia_adn = record.seq
                longitud = len(secuencia_adn)
                try:
                    contenido_gc = calcular_gc(secuencia_adn)
                    secuencia_proteina = traducir_a_proteina(secuencia_adn)
                    informe = (
                        f"==================================================\n"
                        f"ANÁLISIS DE LA SECUENCIA: {id_secuencia}\n"
                        f"==================================================\n"
                        f"Estado: Procesada Correctamente\n"
                        f"Longitud de la secuencia: {longitud} pb\n"
                        f"Contenido GC: {contenido_gc:.2f} %\n"
                        f"protein translation: amino acid sequence\n"
                        f"{secuencia_proteina}\n\n"
                    )
                    num_secuencias_procesadas += 1

                except TranslationError as e:
                   
                    num_secuencias_con_error += 1
                   
                    informe = (
                        f"==================================================\n"
                        f"ANÁLISIS DE LA SECUENCIA: {id_secuencia}\n"
                        f"==================================================\n"
                        f"Estado: ERROR AL PROCESAR\n"
                        f"Longitud de la secuencia: {longitud} pb\n"
                        f"Motivo del error: {e}\n"
                        f"La secuencia probablemente contiene caracteres no válidos (ej. 'X').\n\n"
                    )

                archivo_salida.write(informe)

            print("\n--- Resumen del Análisis ---")
            print(f"Secuencias procesadas con éxito: {num_secuencias_procesadas}")
            print(f"Secuencias con errores: {num_secuencias_con_error}")
            print(f"Resultados completos guardados en: '{ruta_salida}'")

    except FileNotFoundError:
        print(f"Error: El archivo de entrada '{ruta_entrada}' no fue encontrado.")
    except Exception as e:
        print(f"Ha ocurrido un error crítico inesperado: {e}")
def main():
    if len(sys.argv) == 3:
        archivo_entrada = sys.argv[1]
        archivo_salida = sys.argv[2]
    elif len(sys.argv) == 2:
        archivo_entrada = sys.argv[1]
        archivo_salida = "analisis_resultados.txt"
    else:
        archivo_entrada = "multi_secuencia.fasta"
        archivo_salida = "analisis_resultados.txt"
        
    print("\n--- Iniciando Analizador de Secuencias v2.1 (Robusto) ---")
    analizar_archivo_fasta(archivo_entrada, archivo_salida)
    print("------------------------------------------------------\n")

if __name__ == "__main__":
    main()
