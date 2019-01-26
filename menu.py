# coding=utf-8
"""
Fecha:18 de diciembre del 2018

@author: Daniel Quesada Vindas

@ITCR_sede_San_Carlos

@Funcion:Menu principal
"""

import time
import os                       #para funciones del sistema (linux en este caso)--> limpiar pantalla se usara
from tqdm import tqdm           #para la barra de progreso--pip install tqdm--repositorio en github
import menu_espacios as esp     #script que guarda la cantidad de espacios de estacionamiento y los parametros de cada uno



def func_menu_inicial():
    os.system('clear')
    #Barra de progreso que realmente no sirve para nada...
    for i in tqdm(range(20)):
        time.sleep(0.05)
    os.system('clear')
    print'\n\n' 
    print'                                 _________'
    print'                          _.--\"\"\'-----,   `\"--.._'
    print'                       .-\'\'   _/_      ; .\'\"----,`-,'
    print'                     .\'      :___:     ; :      ;;`.`.'
    print'                    .      _.- _.-    .\' :      ::  `..'
    print'                 __;..----------------\' :: ___  ::   ;;'
    print'            .--\"\". \'           ___.....`:=(___)-\' :--\'`.'
    print'          .\'   .\'         .--\'\'__       :       ==:    ;'
    print'      .--/    /        .\'.\'\'     ``-,   :         :   \'`-.'
    print'   .\"\', :    /       .\'-`\\\       .--.\ :         :  ,   _\\'
    print'  ;   ; |   ;       /:\'  ;;      /__  \\\:         :  :  /_\\\ '
    print'  |\_/  |   |      / \__//      /"--\\\ \:         :  : ;|`\|'
    print'  : "  /\__/\____//   """      /     \\\ :         :  : :|\'||'
    print'["""""""""--------........._  /      || ;      __.:--\' :|//|'
    print' "------....______         ].\'|      // |--\"\"\"\'__...-\'`\ \//'
    print'   `|TECNOLABS|__;_...--\'\": :  \    //  |---\"\"\"      \__\_/'
    print'     \"\"\"\"\"\"\"\"\"\'            \ \  \_.//  /'
    print'       `---\'                \ \_     _\''
    print'                             `--`---\'  '

    print'\n'
    time.sleep(0.33)
    print'________                .__       .__   '
    print'\______ \ _____    ____ |__| ____ |  |  '
    print' |    |  \\__   \  /    \|  |/ __ \|  |  '
    print' |    `   \/ __ \|   |  \  \  ___/|  |__'
    print'/_______  (____  /___|  /__|\___  >____/'
    print'        \/     \/     \/        \/      '
    time.sleep(0.33)
    print'________                                    .___       '
    print'\_____  \  __ __   ____   ___________     __| _/____   '
    print' /  / \  \|  |  \_/ __ \ /  ___/\__  \   / __ |\__  \  '
    print'/   \_/.  \  |  /\  ___/ \___ \  / __ \_/ /_/ | / __ \_'
    print'\_____\ \_/____/  \___  >____  >(____  /\____ |(____  /'
    print'       \__>           \/     \/      \/      \/     \/ '
    time.sleep(0.33)
    print'____   ____.__            .___              '
    print'\   \ /   /|__| ____    __| _/____    ______'
    print' \   Y   / |  |/    \  / __ |\__  \  /  ___/'
    print'  \     /  |  |   |  \/ /_/ | / __ \_\___ \ '
    print'   \___/   |__|___|  /\____ |(____  /____  >'
    print'                   \/      \/     \/     \/ '
    print'\n'
    time.sleep(0.33)

    #Barra de progreso que realmente no sirve para nada...
    for i in tqdm(range(100)):
        time.sleep(0.01)
        
    print'\n\n'

    nada = raw_input("Presione la tecla Enter para continuar...")
    
######################Termina funcion menu inicial######################    


def func_menu_opciones():
    os.system('clear')
    #Barra de progreso que realmente no sirve para nada...
    for i in tqdm(range(20)):
        time.sleep(0.05)
    os.system('clear')
    print'               ___  ___ _____ _   _ _   _                 '
    print'               |  \/  ||  ___| \ | | | | |                '
    print'               | .  . || |__ |  \| | | | |                '
    print'               | |\/| ||  __|| . ` | | | |                '
    print'               | |  | || |___| |\  | |_| |                '
    print'               \_|  |_/\____/\_| \_/\___/                 '
    print'\n'                                                          
    print'______                     _                _             '
    print'| ___ \                   (_)              | |            '
    print'| |_/ /_ _ _ __ __ _ _   _ _ _ __ ___   ___| |_ _ __ ___  '
    print'|  __/ _` | \'__/ _` | | | | | \'_ ` _ \ / _ \ __| \'__/ _ \ '
    print'| | | (_| | | | (_| | |_| | | | | | | |  __/ |_| | | (_) |'
    print'\_|  \__,_|_|  \__, |\__,_|_|_| |_| |_|\___|\__|_|  \___/ '
    print'                  | |                                     '
    print'                  |_|                                     '
    print'\n\n'
    time.sleep(0.2)
    print' ____ ____ ____ ____ ____ ____ ____ ____ ____ '
    print'||O |||p |||c |||i |||o |||n |||e |||s |||: ||'
    print'||__|||__|||__|||__|||__|||__|||__|||__|||__||'
    print'|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|'
    print'\n'
    time.sleep(0.2)
    print'NOTA: presione la tecla Q para salir de cualquiera de las opciones que seleccione'
    print'\n'
    time.sleep(0.2)
    try:
        print"Espacios de estacionamiento configurados: {}".format(esp.n_esp)
    except:
        print"Espacios de estacionamiento configurados: {}".format(0)
    print'\n\n\n'
    time.sleep(0.33)
    print'1. Mostrar video en tiempo real'
    time.sleep(0.2)
    print'2. Configuracion de parametros de los espacios (Obligatorio)'
    time.sleep(0.2)
    print'3. Iniciar deteccion de vehiculos [modo grafico] (Opcion 2 obligatoria)'
    time.sleep(0.2)
    print'4. Definir parametros (% video || IP)'
    time.sleep(0.2)
    print'5. Iniciar deteccion de vehiculos [modo consola] (Opcion 2 obligatoria)'
    time.sleep(0.2)
    print'\n'
    print'...o ingrese \"cerrar\" para cerrar el programa\n'
    
   
def cerrando_logo():
        os.system('clear')
        time.sleep(0.5)
        print'\n\n\n'
        print' ██████╗███████╗██████╗ ██████╗  █████╗ ███╗   ██╗██████╗  ██████╗          '
        print'██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔═══██╗         '
        print'██║     █████╗  ██████╔╝██████╔╝███████║██╔██╗ ██║██║  ██║██║   ██║         '
        print'██║     ██╔══╝  ██╔══██╗██╔══██╗██╔══██║██║╚██╗██║██║  ██║██║   ██║         '
        print'╚██████╗███████╗██║  ██║██║  ██║██║  ██║██║ ╚████║██████╔╝╚██████╔╝██╗      '
        print' ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝      '
        time.sleep(0.5)
        os.system('clear')
        print'\n\n\n'
        print' ██████╗███████╗██████╗ ██████╗  █████╗ ███╗   ██╗██████╗  ██████╗          '
        print'██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔═══██╗         '
        print'██║     █████╗  ██████╔╝██████╔╝███████║██╔██╗ ██║██║  ██║██║   ██║         '
        print'██║     ██╔══╝  ██╔══██╗██╔══██╗██╔══██║██║╚██╗██║██║  ██║██║   ██║         '
        print'╚██████╗███████╗██║  ██║██║  ██║██║  ██║██║ ╚████║██████╔╝╚██████╔╝██╗██╗   '
        print' ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝╚═╝   '
        time.sleep(0.5)
        os.system('clear')
        print'\n\n\n'
        print' ██████╗███████╗██████╗ ██████╗  █████╗ ███╗   ██╗██████╗  ██████╗          '
        print'██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔═══██╗         '
        print'██║     █████╗  ██████╔╝██████╔╝███████║██╔██╗ ██║██║  ██║██║   ██║         '
        print'██║     ██╔══╝  ██╔══██╗██╔══██╗██╔══██║██║╚██╗██║██║  ██║██║   ██║         '
        print'╚██████╗███████╗██║  ██║██║  ██║██║  ██║██║ ╚████║██████╔╝╚██████╔╝██╗██╗██╗'
        print' ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝╚═╝╚═╝'
        time.sleep(0.5)
        os.system('clear')




	

#while true 

#func_menu_inicial()

#func_menu_opciones()
