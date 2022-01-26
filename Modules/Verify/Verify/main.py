from Verify import hash_passwd
import click

@click.command()
@click.option("--passwd", help="your password", prompt="Your password")
def main(passwd):
    """ Funkcja printująca hasło po zaszyfrowaniu.

        Parameters:
            passwd String: Hasło

        returns:
            None

    """
    _salt, _hash = hash_passwd(passwd)
    print(f"salt={_salt}\nhash={_hash}")
    return None

if __name__ == "__main__":
    main()
