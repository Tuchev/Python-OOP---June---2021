_PAGE_PHOTOS = 4
_SUCCESS = "photo added successfully on page"
_FAILED = "No more free slots"
_DASHES = f"{11 * '-'}\n"

class PhotoAlbum:
    PAGE_PHOTOS = _PAGE_PHOTOS
    SUCCESS = _SUCCESS
    FAILED = _FAILED
    DASHES = _DASHES

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]
        self.photo_idx = 0

    @classmethod
    def from_photos_count(cls, photo_count: int):
        pages = photo_count // cls.PAGE_PHOTOS
        return cls(pages)

    def is_space(self) -> bool:
        return self.photo_idx < self.pages and len(self.photos[self.photo_idx]) < self.PAGE_PHOTOS

    def page_new(self) -> int:
        if len(self.photos[self.photo_idx]) == self.PAGE_PHOTOS:
            self.photo_idx += 1
        return self.photo_idx

    def add_photo(self, label: str) -> str:
        if not self.is_space():
            return self.FAILED
        self.photos[self.photo_idx].append(str(label))
        photo_added = f"{label} {self.SUCCESS} {self.photo_idx + 1} slot {len(self.photos[self.photo_idx])}"
        self.page_new()
        return photo_added

    def display(self):
        display = self.DASHES
        for _ in self.photos:
            if _:
                display += "".join('[] ' for p in range(len(_))).strip()
            display += f'\n{self.DASHES}'
        return display


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
