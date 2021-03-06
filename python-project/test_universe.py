from universe import count_all_stars
import builtins


sum_builtin_used = False


def new_sum(x):
    global sum_builtin_used
    sum_builtin_used = True
    return orig_sum(x)


orig_sum = builtins.sum
builtins.sum = new_sum


def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test_count_all_stars():
    try:
        count1 = count_all_stars([2, 3])
        assert count1 == 5, "Running count_all_stars([2, 3])... Expected 5, got {}".format(count1)
        count2 = count_all_stars([9, -3])
        assert count2 == 6, "Running count_all_stars([9, -3])... Expected 6, got {}".format(count2)
        success()

        if sum_builtin_used:
            send_msg("My personal Yoda, you are. π", "* β ΒΈ .γΒΈ. :Β° βΎ Β° γΒΈ. β ΒΈ .γγΒΈ.γ:. β’ ")
            send_msg("My personal Yoda, you are. π", "           γβ Β°  β ΒΈ. ΒΈ γβγ :.γ .   ")
            send_msg("My personal Yoda, you are. π", "__.-._     Β° . .γγγγ.γβΎ Β° γ. *   ΒΈ .")
            send_msg("My personal Yoda, you are. π", "'-._\\7'      .γγΒ° βΎ  Β° γΒΈ.β  β .γγγ")
            send_msg("My personal Yoda, you are. π", " /'.-c    γ   * β  ΒΈ.γγΒ°     Β° γΒΈ.    ")
            send_msg("My personal Yoda, you are. π", " |  /T      γγΒ°     Β° γΒΈ.     ΒΈ .γγ  ")
            send_msg("My personal Yoda, you are. π", "_)_/LI")
        else:
            send_msg("Kudos π", "Did you know that you could use the sum function? Try it!")
            send_msg("Kudos π", "")
            send_msg("Kudos π", "galaxies = [37, 3, 2]")
            send_msg("Kudos π", "total_stars = sum(galaxies)  # 42")
    except AssertionError as e:
        fail()
        send_msg("Oops! π", e)
        send_msg("Hint π‘", "Did you properly accumulate all stars into 'total_stars'? π€")


if __name__ == "__main__":
    test_count_all_stars()
