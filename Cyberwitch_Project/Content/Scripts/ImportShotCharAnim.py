import sys

sys.path.append("//medusa/cyberwitch/assets/Scripts/Python/")

import ueImport
reload(ueImport)

seq = "AAA"
shot = "008"

ueImport.importShotAnimations(seq, shot)