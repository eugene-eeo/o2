import pytest
from o2 import Index


@pytest.fixture
def mock(tmpdir):
    p = tmpdir.mkdir('tmp')
    return Index(str(p.join('test.db'))), p


def test_index_iter(mock):
    index, tmpdir = mock
    f1 = tmpdir.join('f1.txt')
    f2 = tmpdir.join('f2.txt')

    f1.write('')
    f2.write('')

    paths = [str(f1), str(f2)]

    index.update(paths)
    assert set(index) == set(paths)


def test_index_has_changed(mock):
    index, tmpdir = mock
    f = tmpdir.join('file.txt')
    f.write('a')
    index.update([str(f)])

    assert not index.has_changed(str(f))

    f.write('b')
    assert index.has_changed(str(f))


def test_index_changed(mock):
    index, tmpdir = mock

    f1 = tmpdir.join('f1.txt')
    f2 = tmpdir.join('f2.txt')

    f1.write('a')
    f2.write('a')

    index.update([str(f1), str(f2)])
    assert index.changed == []

    f1.write('b')
    f2.write('b')
    assert set(index.changed) == {str(f1), str(f2)}
