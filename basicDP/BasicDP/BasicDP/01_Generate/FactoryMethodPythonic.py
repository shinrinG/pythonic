def main():
    cow_factory = Factory(Cow)
    cow_factory.check_animal()

    chiken_factroy = Factory(Chicken)
    chiken_factroy.check_animal()


class Factory:
    def __init__(self, animal_class):
        self.animal = animal_class()

    def check_animal(self):
        self.animal.eat()
        self.animal.speak()


# * Animalクラスを継承しなくなった
# クラスの中身は1コ目のサンプルコードと同じであるため省略
class Cow:
    pass


# * Animalクラスを継承しなくなった
# クラスの中身は1コ目のサンプルコードと同じであるため省略
class Chicken:
    pass


if __name__ == "__main__":
    main()
