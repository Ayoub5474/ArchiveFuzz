import requests


def connector(url):
    result = False
    try:
        # TODO control request headers in here
        response = requests.get(url, timeout=30)
        result = response.text
    except requests.ConnectionError as e:
        raise ConnectionError("\u001b[31;1mCan not connect to server. Check your internet connection\u001b[0m")
    except requests.Timeout as e:
        raise TimeoutError("\u001b[31;1mOOPS!! Timeout Error\u001b[0m")
    except requests.RequestException as e:
        raise AttributeError("\u001b[31;1mError in HTTP request\u001b[0m")
    except KeyboardInterrupt:
        raise KeyboardInterrupt("\u001b[31;1mInterrupted by user\u001b[0m")
    except Exception as e:
        raise RuntimeError("\u001b[31;1m%s\u001b[0m" % (e))
    finally:
        if not result:
            print("\u001b[31;1mCan not get target information[0m")
            print("\u001b[31;1mIf you think this is a bug or unintentional behaviour. Report here : https://github.com/devanshbatham/ArchiveFuzz/issues\u001b[0m")
        return result