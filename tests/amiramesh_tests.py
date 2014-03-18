from nose.tools import *

from amiramesh import *

n = Node(1,2,3);
p = Point3D(1,2,3);
p2 = Point3D(2,3,4);
e = Segment("0","0");
s = Skeleton();
io = AmirameshReader();

def test_node():
    assert_is_instance(n, Node)
    assert_equal(n.x,1)
    assert_equal(n.y,2)
    assert_equal(n.z,3)
    n.x = 4
    assert_equal(n.x,4)

def test_point3d():
    assert_is_instance(p, Point3D)
    assert_equal(p.x,1)
    assert_equal(p.y,2)
    assert_equal(p.z,3)
    p.x = 4
    assert_equal(p.x,4)

    pp = p.list()
    assert_equal(len(pp),3)
    assert_equal(pp[2],3)

    p.add_diameter(3)
    p.add_diameter(4)
    assert_equal(p.diameters[1],4)

def test_segment():
    assert_is_instance(e, Segment)
    e.pointcount = 2
    assert_equal(e.pointcount,2)
    assert_equal(len(e),2)

def test_skeleton():
    assert_is_instance(s, Skeleton)
    s.add_node("0", n)
    s.add_segment(e)
    s.add_points([p,p2])
    s.info()

def test_io():
    assert_is_instance(io, AmirameshReader)
    f = open('data/lariat.am')
    skel = io.parse(f)
    assert_equal(skel.segments[0].pointcount,12)
    assert_equal(skel.segments[1].pointcount,12)
    assert_equal(len(skel.segments[0].points),12)
    assert_equal(len(skel.segments[1].points),12)
