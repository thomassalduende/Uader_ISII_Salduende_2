class Target:
    """
    The Target defines the domain-specific interface used by the client code.
    """
    def request(self) -> str:
        return "Objetivo: el comportamiento correcto del objetivo predeterminado."


class Adaptee:
    """
    The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation before the
    client code can use it.
    """

    def specific_request(self) -> str:
        return "IMDH :otreuP"


class Adapter(Target, Adaptee):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface via multiple inheritance.
    """

    def request(self) -> str:
        return f"Adaptador:  {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    """
    The client code supports all classes that follow the Target interface.
    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Cliente: puedo trabajar bien con los objetos de destino:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Cliente: la clase Adaptee tiene una interfaz extraña. "
          "Mira, no lo entiendo:")
    print(f"Adaptador: {adaptee.specific_request()}", end="\n\n")

    print("Cliente: Pero puedo trabajar con él a través del Adaptador:")
    adapter = Adapter()
    client_code(adapter)

