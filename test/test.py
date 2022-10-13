import kunai


def test_timeit():
    with kunai.utils.TimeIt("hoge"):
        print("timeit with statement")

    @kunai.utils.timeit("fuga")
    def _timeit():
        print("timeit decorater")

    _timeit()
