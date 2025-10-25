markdown
    # 🔬 Analizador Básico de Secuencias de ADN

    Un script simple creado con Python y la librería Biopython para realizar un análisis fundamental de secuencias de ADN a partir de un archivo en formato FASTA.

    Este proyecto fue creado como parte de mi portafolio de bioinformática.

    ## Funcionalidades

    *   Lee una única secuencia desde un archivo `.fasta`.
    *   Calcula la longitud total de la secuencia en pares de bases (pb).
    *   Calcula el contenido porcentual de Guanina y Citosina (GC).
    *   Traduce la secuencia de ADN a su correspondiente secuencia de proteína.

    ## Herramientas Utilizadas

    *   Python 3.9
    *   Biopython
    *   Anaconda

    ## Cómo Usarlo

    Sigue estos pasos para ejecutar el programa en tu propia máquina.

    1.  **Clona el repositorio:**
        ```bash
        git clone https://github.com/[JacsonAFP]/Analizador-Secuencias-ADN.git
        cd Analizador-Secuencias-ADN
        ```

    2.  **Crea y activa el entorno de Conda:**
        ```bash
        conda create --name fasta-analyzer python=3.9 biopython
        conda activate fasta-analyzer
        ```

    3.  **Ejecuta el script:**
        El script usará el archivo `secuencia_ejemplo.fasta` por defecto.
        ```bash
        python analizador_adn.py
        ```

    ## Salida de Ejemplo

    ```
    ==================================================
    🔬 ANÁLISIS DE LA SECUENCIA: secuencia_prueba_gen_ABC1
    ==================================================

    🧬 Longitud de la secuencia de ADN: 562 pb
    📊 Contenido GC: 33.45 %

    --------------------------------------------------

    ************* TRANSLACIÓN A PROTEÍNA *************

    MRDRDR*R*TDR*TDR... (etc)
    ```
    ```

