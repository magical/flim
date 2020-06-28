from .flim import decode_flim

def _main():
    import sys
    input = sys.argv[1]
    with open(input, "rb") as f:
        data = f.read()
    img = decode_flim(data)
    img.write_to_png(sys.stdout.buffer)

_main()    
