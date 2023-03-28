class Video:
    def create(self, name):
        self.name = name

    def play(self):
        print(f"Playing video {self.name}")

class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video: Video) -> None:
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx: int) -> None:
        cls.videos[video_indx].play()


v1, v2 = Video(), Video()

v1.create("Python")
v2.create("Python OOP")

YouTube.add_video(v1)
YouTube.add_video(v2)

YouTube.play(0)
YouTube.play(1)
