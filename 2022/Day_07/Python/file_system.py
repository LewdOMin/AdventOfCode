from typing import List, Optional, Union


class Filesystem(object):
    def __init__(self):
        self.__ROOT = Folder('/')   # type: Folder
        self._current_path = ''     # type: str
        self.current_dir = None     # type: Optional[Folder]

    def __iter__(self):
        content = [item for item in self.__ROOT]
        index = -1
        while index + 1 < len(content):
            index += 1
            if type(content[index]) is Folder:
                content.extend([el for el in content[index]])
            yield content[index]

    def get_size(self):
        return self.__ROOT.get_size()

    def make_directory(self, name):
        # type: (str) -> None
        self.current_dir.add_item(Folder(name))

    def make_file(self, name, size):
        # type: (str, int) -> None
        self.current_dir.add_item(File(name, size))

    def change_directory(self, path):
        # type: (str) -> None
        if self.current_dir is None:
            if path != self.__ROOT.get_name():
                raise SyntaxError('Path does not exist!')

            self._current_path = '/'
            self.current_dir = self.__ROOT
        else:
            if path in self.current_dir:
                self.current_dir = self.current_dir.get_item(path)
            elif path == '..':
                self.current_dir = self.current_dir.get_owner()


class Item(object):
    def __init__(self, name, content):
        self._content = content     # type: Optional[Union[List[Item], int]]
        self._owner = None          # type: Optional[Folder]
        self._name = name           # type: str

    def __repr__(self):
        return self._name + (' ' + str(self._content) if type(self._content) is int else '')

    def __str__(self):
        return self.__repr__()

    def get_size(self):
        # type: () -> int
        raise NotImplementedError()

    def _set_owner(self, owner):
        # type: (Folder) -> None
        self._owner = owner

    def get_owner(self):
        # type: () -> Folder
        return self._owner

    def get_name(self):
        # type: () -> str
        return self._name


class File(Item):
    def __iter__(self):
        raise TypeError()

    def get_size(self):
        return int(self._content)


class Folder(Item):
    def __init__(self, name):
        super(Folder, self).__init__(name, None)
        self._content = []

    def __iter__(self):
        for item in self._content:
            yield item

    def __contains__(self, name):
        if type(name) is not str:
            raise TypeError()
        return any(item.get_name() == name for item in self._content)

    def get_size(self):
        return sum([item.get_size() for item in self._content])

    def add_item(self, item):
        # type: (Item) -> None
        self._content.append(item)
        item._set_owner(self)

    def get_item(self, name):
        # type: (str) -> Optional[List[Item]]
        if name not in self:
            return None

        for item in self._content:
            if name == item.get_name():
                return item

        return None