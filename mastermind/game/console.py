class Console:

    def _read(self, message):
        return input(message)



    def _write(self, text):
        return print(text)

    def _check_guess(self, guess):
        if len(guess) != 4:
            return False

        else:
            return True
        

    def _check_if_win(self, hint):
        if hint == "xxxx":
            return True
        else:
            return False
