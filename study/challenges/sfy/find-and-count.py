
INPUT = """ana,song1,0000000001
ana,song2,0000000002
john,song1,0000000003
ana,song3,0000000004
bob,song4,0000000005
bob,song1,0000000006
bob,song3,0000000007
bob,song2,0000000007
john,song1,0000000003
john,song2,0000000003
john,song3,0000000003
john,song5,0000000003
maria,song5,0000000003
maria,song6,0000000003
"""


def process():
    _in = INPUT.splitlines()
    user_song_map = {}                                                  # O(N)
    for i in _in:                                                       # O(N)
        user, song, _ = i.split(',')
        if user in user_song_map:
            user_song_map[user] += [song]
        else:
            user_song_map[user] = [song]

    # O(N/3) ~ O(N)
    cache = {}
    max_ = ['', 0]
    for songs in user_song_map.values():                                # O(N)
        total_len = len(songs)
        start_idx = 0
        end_idx = min(3, total_len)
        # O(N-3) -> O(N*(N-3)) ~ O(N**2)
        while end_idx <= total_len:
            curr_sub_song_set = ','.join(songs[start_idx: end_idx])
            if curr_sub_song_set in cache:
                val = cache[curr_sub_song_set] + 1
            else:
                val = 1

            cache[curr_sub_song_set] = val
            if val > max_[1]:
                max_ = [curr_sub_song_set, val]

            start_idx += 1
            end_idx += 1

    return max_


def process2():
    song_input = INPUT.splitlines()
    user_song_map = {}
    cache = {}
    max_frequency = ['', 0]
    # O(N)
    for i in song_input:
        user, song, _ = i.split(',')
        if user in user_song_map:
            user_song_map[user].append(song)
            if len(user_song_map[user]) >= 3:
                stringyfied_subset = ','.join(user_song_map[user][-3:])
                if stringyfied_subset in cache:
                    val = cache[stringyfied_subset] + 1
                else:
                    val = 1

                cache[stringyfied_subset] = val
                if val > max_frequency[1]:
                    max_frequency = [stringyfied_subset, val]
        else:
            user_song_map[user] = [song]

    return max_frequency


if __name__ == "__main__":
    print(process())
    print(process2())
