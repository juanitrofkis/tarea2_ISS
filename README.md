# tarea2_ISS

## Descripción 


## Tabla de contenidos 
<a name="general-info"></a>
-[Sistema_Operativo](#Sistema_Operativo)
-[Instalación_JACK2](#Instalación_JACK2)
-[Instalación_Chuck](#Instalación_Chuck)
-[Instalación_Pure_Data](#Instalación_Pure_Data)
-[Configuración_JACK2](#Configuración_JACK2)
-[Comandos_Escenario_1](#Comandos_Escenario_1)
-[Comandos_Escenario_2](#Comandos_Escenario_2)
-[Ejemplos_Básico_Chuck](#Ejemplos_Básico_Chuck)
-[Ejemplos_Básico_PureData](#Ejemplos_Básico_PureData)
-[Archivos_desinstalación](#Archivos_desinstalación)
## Sistema_Operativo
Esta comprabado el funcionamiento para el sistema operativo Linux Ubuntu 22.04.
## Instalación_JACK2
1. Clonar el repositorio de github de JACK2
   ```bash
    git clone https://github.com/jackaudio/jack2
    cd jack2
2. Modificar el archivo waf para cambiar la versión de pyhton
     ```bash
    nano/code/gedit waf
    python --> python3
3. Descargar el repositorio en el mismo directorio que se ha clonado JACK2 y ejecutar el install_jackd.sh
   ```bash
    git clone 
    ./install_jackd.sh
Otra opción es instalarlo usted para ello hay que hacer:
1. Clonar el repositorio de github de JACK2
   ```bash
    git clone https://github.com/jackaudio/jack2
    cd jack2
2. Modificar el archivo waf para cambiar la versión de pyhton
   ```bash
    nano/code/gedit waf
    python --> python3
3. Instalar dependendencias necesarias
   ```bash
    sudo apt-get update
    sudo apt-get install -y libopus-dev portaudio19-dev libasound2-dev libffado-dev libgtkmm-2.4-dev libeigen3-dev
4. Configurar e instalar JACK
   ```bash
    ./waf configure
    ./waf build
    sudo ./waf install
5. Configurar JACK para habilitar soporte ALSA y PortAudio
   ```bash
    sudo cp build/jackd ~/.jackdrc
    echo "driver alsa" | sudo tee -a ~/.jackdrc
    echo "driver real_time 1" | sudo tee -a ~/.jackdrc
    echo "driver seq" | sudo tee -a ~/.jackdrc
    echo "realtime-priority 99" | sudo tee -a ~/.jackdrc
    echo "realtime" | sudo tee -a ~/.jackdrc
    echo "softmode" | sudo tee -a ~/.jackdrc
6. Configurar el límite de archivos para permitir la ejecución en tiempo real
   ```bash
    echo "@audio   -  rtprio     99" | sudo tee -a /etc/security/limits.conf
    echo "@audio   -  memlock    unlimited" | sudo tee -a /etc/security/limits.conf
7. Configura el kernel para permitir el acceso en tiempo real
   ```bash
    sudo echo "snd-aloop" | sudo tee -a /etc/modules
    echo "options snd-aloop index=0 pcm_substreams=2" | sudo tee -a /etc/modprobe.d/alsa-loopback.conf
    sudo update-initramfs -u
8. Añadir el usuario dit al grupo audio
   ```bash
    usermod -a -G audio dit
9. Comprobar versión de JACK2
   ```bash
    jackd --version
10. Instalar herramienta gráfica
     ```bash
      sudo apt-get install qjackctl

## Instalación_Chuck
Para instalar el sintentizador Chuck hay que seguir los siguientes pasos:
1. Descargar el fichero .tar de la siguiente URL: https://chuck.cs.princeton.edu
2. Descomprimir el fichero tar
   ```bash
    tar -xvzf chuck-1.5.1.8.tgz
    cd chuck-1.5.1.8
3. Instalar dependencias
   ```bash
   sudo apt install -y build-essential bison flex libsndfile1-dev \
    libasound2-dev libpulse-dev libjack-jackd2-dev
4. Ingresar en el directorio src y compilar Chuck
   ```bash
    make linux
5. Verficar instalación
   ```bash
    ./chuck --version
Otra opción es descargar de este repositorio el fichero de la versión 1.5.1.8 de Chuck y utilizar el install_chuck.sh, en el mismo directorio en donde este archivo comprimido chuck-1.5.1.8.tgz:
1. ```bash
    ./install_chuck.sh
## Instalación_Pure_Data 
Para instalar el sintentizador Pure Data hay que seguir los siguientes pasos:
1. Clonar el repositorio
    ```bash 
     git clone https://github.com/pure-data/pure-data.git
2. Instalar dependencias
   ```bash
    sudo apt-get update
    sudo apt-get install build-essential tcl tk
    sudo apt-get install libasound2-devv
3. Ingresar en el directorio de pure-data y compilar Pure Data
   ```bash
    ./autogen.sh
    ./configure --enable-jack
    make
    sudo make install
4. Verficar instalación
   ```bash
    ./pd --version
Otra opción es descargar de este repositorio el fichero install_pureData.sh
1. ```bash
    ./install_pureData.sh
## Comandos_Escenario_1 
1. ```bash
    qjackctl
    otra terminal: cd /dir/ejecutable/chuck
                   ./chuck --driver:jack /dir/archivo.ck
    otra terminal: cd /dir/ejecutable/pure-data
                   ./pd -jack
## Comandos_Escenario_2 
1. Ordenador Maestro
    ```bash
    qjackctl
    jack_load netmanager
2. Ordenador Esclavo-Pure Data
    ```bash
    jackd -d net -a ip_multicast -p port
    qjackctl
    ./pd -jack

3. Ordenador Esclavo-Chuck
    ```bash
    jackd -d net -a ip_multicast -p port
    qjackctl
    ./chuck --driver:jack /dir/test_prueba.ck
## Ejemplos_Básico_Chuck
Se ha añadido un archivo test_chuck.ck, que es un ejemplo básico de la transmisión de un pitido para comprobar el correcto funcionamiento de JACK2 con Chuck.
## Ejemplos_Básico_PureData
Se han añadido dos archivos de Pure Data, en donde el primero estan las distintas escalas músicales y algunos parámetros para poder variar la intesidad del sonido y luego también se ha añadido un ejemplo básico de la transmisión de un pitido para comprobar el correcto funcionamiento de JACK2 con Pure Data.
## Archivos_desinstalación
Se ha añadido una carpeta, llamada archivos_uninstall, donde hay tres scripts sh, para poder ejecutarlos y desisntalar el servicio de JACK2 y los sintetizadores Pure Data y Chuck. Primero se aconseja desinstalar JACK2 y después los dos sintetizadores. 
