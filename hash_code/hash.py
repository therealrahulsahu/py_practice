class Library:
    def __init__(self, lib_id, meta, book_code):
        self.lib_id = lib_id
        self.n_books = meta[0]
        self.n_sign_days = meta[1]
        self.books_per_day = meta[2]

        self.book_id = book_code
        self.days_left = 0


files = ['a_example.txt', 'b_read_on.txt', 'c_incunabula.txt', 'd_tough_choices.txt', 'e_so_many_books.txt', 'f_libraries_of_the_world.txt']

for file_name in files:
    data_file = open(file_name, 'r')
    n_books, n_lib, n_days = list(map(int, data_file.readline().split()))
    score_books = list(map(int, data_file.readline().split()))
    lib_data = []
    for lib_id in range(n_lib):
        lib_meta = list(map(int, data_file.readline().split()))
        lib_books = list(map(int, data_file.readline().split()))
        books_with_score = []
        for b_id in lib_books:
            books_with_score.append([b_id, score_books[b_id]])
        in_pair = sorted(books_with_score, key=lambda x: x[1], reverse=True)
        books = [x[0] for x in in_pair]
        lib_data.append(Library(lib_id, lib_meta, books))
    data_file.close()

    sort_lib = sorted(lib_data, key=lambda x: (-1*(1/x.n_sign_days)*x.n_books*x.books_per_day))

    books_queue = []

    days_left = n_days
    to_execute = []
    out_str = ''
    lib_count = 0
    for lib in sort_lib:
        in_books = lib.book_id.copy()
        selected_books = []
        left_books = []
        while in_books:
            first = in_books.pop(0)
            if first not in books_queue:
                books_queue.append(first)
                selected_books.append(first)
            else:
                left_books.append(first)
        selected_books.extend(left_books)

        lib.book_id = selected_books.copy()

        if (days_left - lib.n_sign_days > 0) and (len(lib.book_id) > 0):
            lib.days_left = days_left - lib.n_sign_days
            days_left -= lib.n_sign_days

            lib_count += 1
            out_lib_id = lib.lib_id
            out_n_book = lib.days_left * lib.books_per_day
            if out_n_book > lib.n_books:
                out_n_book = lib.n_books
            out_str += str(out_lib_id) + ' ' + str(out_n_book) + '\n'
            out_books_arr = lib.book_id[:out_n_book]
            for x in out_books_arr:
                out_str += str(x) + ' '
            out_str += '\n'
        else:
            break

    out_str = str(lib_count)+'\n' + out_str

    with open('out_'+file_name, 'w') as out_file:
        out_file.write(out_str)
