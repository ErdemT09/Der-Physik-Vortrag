from manim import *
import numpy

class scene7(GraphScene):
    CONFIG = {
        "x_tick_frequency": 0.002,
        "y_tick_frequency": 0.002,
        "x_min": -10,
        "x_max": 15,
        "y_min": 8,
        "y_max": 15,
        #"x_label_decimals": 2,
        "x_label_nums": 1,
        "x_axis_label":"x",
        "y_axis_label":"y"
        }
    def construct(self):
        self.graph_origin = 2*LEFT + 1.5* UP
        self.x_min = -10
        self.y_min = -10
        self.y_max = 2
        self.x_axis_width=16
        self.y_axis_height=10
        self.setup_axes()
        f = self.get_graph(self.func1, color = RED, x_min = 0.1, step_size = 0.0001)
        self.play(Write(f))
        self.wait(1)
        
    def func1(self,x):
        return -5/x



class scene5(Scene):
    def construct(self):
        text = TextMobject(r"Lösung:")
        text.to_corner(UL, buff=0.7)
        self.play(Write(text))

        text1 = TextMobject(r"Ansatz: W = \(GMm (\frac{1}{r_1} - \frac{1}{r_2})\)")
        text1.next_to(text,DOWN, buff = 0.2)
        text1.shift(numpy.array([2.3,0,0]))
        self.play(Write(text1), run_Time = 1)

        text_ = Tex(r"Mit ")
        text_.shift(numpy.array([0.5,0,0]))
        text2 = MathTex(r"r_1 \rightarrow \infty")
        text3 = Tex(r"erhält man ")
        text4 = MathTex(r"\frac{1}{r_1} \rightarrow 0")
        text_.next_to(text1,DOWN, buff = 0.2)
        text2.next_to(text_,RIGHT, buff = 0.3)
        text3.next_to(text2,RIGHT, buff = 0.2)
        text4.next_to(text3,RIGHT, buff = 0.2)
        self.play(Write(text_))
        self.play(Write(text2))
        self.play(Write(text3))
        self.play(Write(text4))

        text1 = MathTex(r"{\Rightarrow}")
        text2 = MathTex(r"W=-\frac{GMm}{r_2}=")
        text3 = Tex(r"-3,13 \textperiodcentered")
        text4 = MathTex(r"10^{10}J")
        text1.to_edge(LEFT)
        text2.next_to(text1, RIGHT, buff=0.3)
        text3.next_to(text2, RIGHT, buff=0.3)
        text4.next_to(text3, RIGHT, buff=0.3)
        text3.shift(numpy.array([0.1,-0.1,0]))
        text4.shift(numpy.array([0,0.0,0]))
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.play(Write(text4))




class scene4(Scene):
    def construct(self):
        text = TextMobject(r"Ein Beispiel für die Rechnung von Arbeit")
        text.to_edge(UP, buff=0.4)
        self.play(Write(text))

        text = TextMobject(r"Welche Arbeit kann ein Meteorid der Masse 500 kg\\ verrichten, der aus den Tiefen des Alls kommt und \\auf die Erdoberfläche fällt?")
        text.scale(1)
        text.to_edge(UP, buff=1.9)
        self.play(Write(text))

        text0 = TextMobject(r"Gesucht: W=?")
        text0.next_to(text,DOWN, buff=0.4)
        text0.shift(np.array([-5,0,0]))
        self.play(Write(text0))
        text1 = TextMobject(r"Gegeben: M = 5,97\textperiodcentered")
        text2 = MathTex(r"10^{24}")
        text3 = TextMobject(r"(Masse der Erde)")
        text1.next_to(text0,DOWN, buff=0.4)
        text1.shift(np.array([0.6,0,0]))
        text2.next_to(text1,RIGHT, buff=0)
        text3.next_to(text2,RIGHT, buff=0.1)
        text2.shift(np.array([0,0.10,0.05]))
        text4 = MathTex(r"r_1 \rightarrow \infty")
        text4.next_to(text1,DOWN, buff=0.25)
        text4.shift(numpy.array([0.9,0,0]))
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.play(Write(text4))

        text1 = MathTex(r"r_2 = {6,371{\textperiodcentered}}")
        text2 = MathTex(r"10^{6}m")
        text3 = TextMobject(r"(Radius der Erde)")
        text1.next_to(text4,DOWN, buff=0.1)
        text1.shift(np.array([0.4,-0.2,0]))
        text2.next_to(text1,RIGHT, buff=0.2)
        text3.next_to(text2,RIGHT, buff=0.1)
        text2.shift(np.array([0,0.10,0.05]))
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))

        text0 = text1
        text1 = MathTex(r"G = {6,67{\textperiodcentered}}")
        text2 = MathTex(r"10^{-11}\frac{m^3}{kg" r" s^2}")
        text1.next_to(text0,DOWN, buff=0.6)
        text1.shift(np.array([-0.3,0,0]))
        text2.next_to(text1,RIGHT, buff=0.2)
        text2.shift(np.array([0,0,0.05]))
        self.play(Write(text1))
        self.play(Write(text2))
        #

class scene3(Scene):
    def construct(self):
        text = TextMobject(r"Arbeit in dem homogenen Gravitationsfeld")
        text.to_edge(UP, buff=1)
        self.play(Write(text))
        text = TextMobject(r"W")
        text.to_corner(UL,buff=2)
        self.play(Write(text), run_Time = 0.5)
        text0 = TextMobject(r"= m\textperiodcentered g\textperiodcentered")
        text0.next_to(text,RIGHT, buff = 0.3)
        text1 = MathTex(r"({h_2}-{h_1})")
        text1.next_to(text0,RIGHT, buff = 0.2)
        self.play(Write(text0),Write(text1), run_Time = 1)

        text1 = TextMobject(r"= m\textperiodcentered g\textperiodcentered $\Delta$h")
        text1.next_to(text,RIGHT, buff = 0.3)
        text1.shift(numpy.array([0,-0.8,0]))
        self.play(Write(text1), run_Time = 1)

        img = ImageMobject("./erd.png")
        img.to_corner(DOWN+RIGHT, buff=0)
        img.shift(numpy.array([0,-1,0]))
        self.play(FadeIn(img))

class scene2(Scene):
    def construct(self):
        text = TextMobject(r"Arbeit in dem inhomogenen Gravitationsfeld")
        text.to_edge(UP, buff=1)
        self.play(Write(text))
        text = TextMobject(r"W")
        text.to_corner(UL,buff=2)
        self.play(Write(text), run_Time = 0.5)
        text0 = TextMobject(r"= \(\int_{r_2}^{r_1} F(r) dr\)")
        text0.next_to(text,RIGHT, buff = 0.3)
        self.play(Write(text0), run_Time = 1)
        self.wait(10)

        text1 = TextMobject(r"= \(\int_{r_2}^{r_1} {\frac{GMm}{r^2} dr}\)")
        text1.next_to(text,RIGHT, buff = 0.3)
        text1.shift(numpy.array([0,-0.8,0]))
        self.play(Write(text1), run_Time = 1)

        text1 = TextMobject(r"= \(GMm \int_{r_2}^{r_1} {\frac{1}{r^2} dr}\)")
        text1.next_to(text,RIGHT, buff = 0.3)
        text1.shift(numpy.array([0,-1.6,0]))
        self.play(Write(text1), run_Time = 1)

        text1 = TextMobject(r"= \(GMm [\frac{-1}{r}]_{r_1}^{r_2}\)")
        text1.next_to(text,RIGHT, buff = 0.3)
        text1.shift(numpy.array([0,-2.4,0]))
        self.play(Write(text1), run_Time = 1)
        
        text1 = TextMobject(r"= \(GMm (\frac{1}{r_1} - \frac{1}{r_2})\)")
        text1.next_to(text,RIGHT, buff = 0.3)
        text1.shift(numpy.array([0,-3.2,0]))
        self.play(Write(text1), run_Time = 1)

    #
class scene6(Scene):
    def construct(self):
        text = TextMobject(r" a")
        text.scale(1.7)
        text.move_to( ORIGIN)
        text_ = MathTex(r"{\Rightarrow}")
        text_.scale(1.7)
        text_.next_to(text, LEFT, 0.2)
        img = ImageMobject("./prop.png")
        img.move_to( np.array([0.7, 0, 0]))
        img.scale(0.9)
        text0 = MathTex(r" \frac{M}{r^2}")
        text0.scale(1.7)
        text0.next_to(img, RIGHT, buff=0)
        text0.shift(np.array([0,0.13,0]))
        self.play(Write(text_), Write(text), FadeIn(img), Write(text0), run_time=2)

        text = TextMobject(r"a=G")
        text1 = MathTex(r"\frac{M}{r^2}")
        text.scale(1.7)
        text1.scale(1.7)
        text.move_to(numpy.array([0,-2,0]))
        text1.next_to(text, RIGHT, buff=0.4)
        self.play(Write(text))
        self.play(Write(text1))

        text1 = MathTex(r"G = {6,67{\textperiodcentered}}")
        text2 = MathTex(r"10^{-11}\frac{m^3}{kg" r" s^2}")
        text1.to_edge(LEFT)
        text1.scale(1.2)
        text2.scale(1.2)
        text1.shift(np.array([-0.3,0,0]))
        text2.next_to(text1,RIGHT, buff=0.2)
        text2.shift(np.array([0,0,0.05]))
        self.play(Write(text1))
        self.play(Write(text2))

class scene1(Scene):
    def construct(self):
        text = MathTex(r" \frac{g_E}{3600} \approx g_{EM}")
        text.scale(1.6)
        text.to_corner(UL, buff=1.5)
        self.play(Write(text), run_time=2)

        text0 = TextMobject(r"(Wie stark die Erdbeschleunigung für Mond ist)")
        text0.scale(0.66)
        text0.next_to(text, RIGHT, buff = 0.3)
        text0.shift(np.array([0,-0.13,0]))
        self.play(Write(text0), run_time=1)

        text = MathTex(r" 60 {r_E} \approx r_{EM}")
        text.scale(1.6)
        text.to_edge(LEFT, buff=1.5)
        self.play(Write(text), run_time=2)

        text0 = TextMobject(r"(Wie weit Mond von dem Massenzentrum der Erde ist)")
        text0.scale(0.66)
        text0.next_to(text, RIGHT, buff = 0.3)
        text0.shift(np.array([0,-0.13,0]))

        text1 = MathTex(r" \{r_E} = 6371km")
        text1.scale(0.66)
        text1.next_to(text0,DOWN, buff = 0.3)
        text2 = MathTex(r" \{r_ {EM} } = 384400km")
        text2.scale(0.66)
        text2.next_to(text1,DOWN, buff = 0.3)
        self.play(Write(text0), run_time=1)
        self.play(Write(text1), run_time=0.5)
        self.play(Write(text2), run_time=0.5)


        self.wait(9)
        text = TextMobject(r" a")
        text.scale(1.7)
        text.move_to( np.array([-4.6, -2.4, 0]))
        text_ = MathTex(r"{\Rightarrow}")
        text_.scale(1.7)
        text_.next_to(text, LEFT, 0.2)
        img = ImageMobject("./prop.png")
        img.move_to( np.array([-3.9, -2.4, 0]))
        img.scale(0.9)
        text0 = MathTex(r" \frac{1}{r^2}")
        text0.scale(1.7)
        text0.next_to(img, RIGHT, buff=0)
        text0.shift(np.array([0,0.13,0]))
        text1 = TextMobject(r"(Abstand zwischen den Körpern)")
        text1.scale(0.9)
        text1.next_to(text0, RIGHT, buff=0.3)
        self.play(Write(text_), Write(text), FadeIn(img), Write(text0), Write(text1), run_time=2)

class scene0(Scene):
    def construct(self):
        text = TextMobject(r"F = m\textperiodcentered a	")
        text.scale(1.6)
        text.to_corner(UL, buff=1.5)
        self.play(Write(text), run_time=2)

        ar = Arrow(np.array([-3.8, 1.8, 0]), np.array([-4.2, 1, 0]), buff=0)
        text = TextMobject(r"Die Masse von dem Körper")
        text.scale(1.3)
        text.move_to(np.array([-4.2, 0.5, 0]))
        self.play(Write(ar), Write(text), run_time=2)

        ar = Arrow(np.array([-2.4, 2.1, 0]), np.array([-1, 2.1, 0]), buff=0)
        text = TextMobject(r"= ?")
        text.scale(1.3)
        text.move_to( np.array([-0.3, 2.2, 0]))
        self.play(Write(ar), Write(text), run_time=2)

        text = TextMobject(r"a")
        text.scale(1.7)
        text.move_to( np.array([-4.6, -1.5, 0]))
        img = ImageMobject("./prop.png")
        img.move_to( np.array([-3.9, -1.5, 0]))
        img.scale(0.9)
        text0 = TextMobject(r"M")
        text0.scale(1.7)
        text0.next_to(img, RIGHT, buff=0)
        text0.shift(np.array([0,0.13,0]))
        text1 = TextMobject(r"(Masse des anziehenden Körpers)")
        text1.scale(0.9)
        text1.next_to(text0, RIGHT, buff=0.3)
        self.play(Write(text), FadeIn(img), Write(text0), Write(text1), run_time=2)

        '''
        square = Square()
        dot1 = Dot()
        self.add(dot1)

        dot1.to_edge(LEFT)
        
        
        self.play(FadeIn(square), run_time=0.5)
        dot1.to_corner(UR, buff=0)
        self.wait(1)
        l = Line(ORIGIN, dot1)
        self.play(FadeIn(l))
        self.remove(square)
        self.wait(0.3)
        rec = Rectangle()
        rec.width = 5.0
        rec.height = 1.0
        rec.color = BLUE
        self.play(FadeIn(rec), run_time=0.5)
        self.remove(text)
        '''
        self.wait(2)