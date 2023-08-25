from pytube import YouTube, exceptions, Stream  # type: ignore
import telegram
import sys

# Available Resolution
# “720p”, “480p”, “360p”, “240p”, “144p”


def main() -> None:
    yt = validate(input("Link: "))
    stream = yt.streams  # type: ignore[attr-defined]
    # select resolution
    reso: str = input("Select Resolution: ")
    # selected video file
    hd: list = stream.filter(res=f"{reso}", progressive=True,
                             type="video")
    # download
    hd[0].download()


def validate(link: str) -> object:
    try:
        yt = YouTube(f"{link}")
        yt.bypass_age_gate()
        return yt
    except exceptions.RegexMatchError:
        sys.exit("Invalid Link")
    except exceptions.AgeRestrictedError:
        sys.exit("Age restricted")


if __name__ == "__main__":
    main()
