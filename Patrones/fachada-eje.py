from __future__ import annotations


class Facade:

    def __init__(self, subvideo1: Video1, subvideo2: Video2) -> None:
        
        self._subvideo1 = subvideo1 or Video1()
        self._subvideo2 = subvideo2 or Video2()

    def operation(self) -> str:

        results = []
        results.append("Fachada inicializa y prepara los videos para realizar la accion: ")

        results.append(self._subvideo1.prepara_video_H264())
        results.append(self._subvideo2.prepara_video_H265())
        return "\n".join(results)


class Video1:

    def prepara_video_H264(self) -> str:
        return "Video H.264 preparado para usar"


class Video2:
   

    def prepara_video_H265(self) -> str:
        return "Video H.265 preparado para usar"


def client_code(facade: Facade) -> None:
    print(facade.operation(), end="")


if __name__ == "__main__":

    subvideo1 = Video1()
    subvideo2 = Video2()
    facade = Facade(subvideo1, subvideo2)
    client_code(facade)
    print("\n")