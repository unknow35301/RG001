import RG001

while True:
    try:
        RG001.main()
    except SystemExit:
        break
    except Exception:
        pass