from pytube import YouTube, exceptions
import sys

available_resolution = ["720p", "480p", "360p", "240p", "144p"]


def main() -> None:
    yt = validate(input("Link: "))
    streams = yt.streams
    reso: str = ""
    # Ensure reso is valid
    while True:
        # select resolution
        reso = input("Select Resolution: ")
        if reso in available_resolution:
            break

    # selected video file
    hd: list = streams.filter(res=f"{reso}", progressive=True, type="video")
    # download
    hd.first().download()


def validate(link: str) -> object:
    try:
        yt = YouTube(f"{link}")
        yt.bypass_age_gate()
    except exceptions.RegexMatchError:
        sys.exit("Invalid Link")
    except exceptions.AgeRestrictedError:
        sys.exit("Age restricted")
    except exceptions.VideoUnavailable:
        sys.exit("Video unavailable")
    except:
        sys.exit("Opps! Something went wrong.")
    return yt


if __name__ == "__main__":
    main()
