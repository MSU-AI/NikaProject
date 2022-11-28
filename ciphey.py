import os
import subprocess

def eval_encryption(text):
    os.environ["PYTHONUTF8"] = "1"
    error_code = 0

    try:
        proc = subprocess.Popen("ciphey -t \"" + text + "\" -q", stdout=subprocess.PIPE)
        (out, err) = proc.communicate()
        out = str(out)
        out = out[2:len(out)-1]
        out = out.replace("\\r\\n", " ")
        error_code = 0
    except:
        out = "*Unknown error occurs during decryption*"
        error_code = 1

    if out == "Failed to crack " or out == "":
        out = "*Failed to crack due to unsupported encoder, language, or other issue*"
        error_code = 1

    return out, error_code

    # test string "aGVsbG8gbXkgbmFtZSBpcyBiZWU="
    # test string "Aopz pz Hukyld zwlhrpun. P sprl abyaslz."