# coding=utf-8
"""
Fecha:15 de diciembre del 2018

@author: Daniel Quesada Vindas

@ITCR_sede_San_Carlos

Menu principal
"""

import time
import sys


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

print'________                .__       .__   '
print'\______ \ _____    ____ |__| ____ |  |  '
print' |    |  \\__   \  /    \|  |/ __ \|  |  '
print' |    `   \/ __ \|   |  \  \  ___/|  |__'
print'/_______  (____  /___|  /__|\___  >____/'
print'        \/     \/     \/        \/      '

print'________                                    .___       '
print'\_____  \  __ __   ____   ___________     __| _/____   '
print' /  / \  \|  |  \_/ __ \ /  ___/\__  \   / __ |\__  \  '
print'/   \_/.  \  |  /\  ___/ \___ \  / __ \_/ /_/ | / __ \_'
print'\_____\ \_/____/  \___  >____  >(____  /\____ |(____  /'
print'       \__>           \/     \/      \/      \/     \/ '

print'____   ____.__            .___              '
print'\   \ /   /|__| ____    __| _/____    ______'
print' \   Y   / |  |/    \  / __ |\__  \  /  ___/'
print'  \     /  |  |   |  \/ /_/ | / __ \_\___ \ '
print'   \___/   |__|___|  /\____ |(____  /____  >'
print'                   \/      \/     \/     \/ '
print'\n'

ancho_barra = 100		#barra de progreso

# setup toolbar
sys.stdout.write("[%s]" % ("-" * ancho_barra))  #el simbolo que va en sobrescribiendo...
sys.stdout.flush()
sys.stdout.write("\b" * (ancho_barra+1)) # return to start of line, after '['

for i in xrange(ancho_barra):
    time.sleep(0.1) # do real work here
    # update the bar
    sys.stdout.write("|")
    sys.stdout.flush()

sys.stdout.write("\n")

