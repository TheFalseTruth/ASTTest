import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_var_decl1(self):
        input = "VAR i: integer;"
        expect = str(Program([VarDecl(Id('i'),IntType())]))
        self.assertTrue(TestAST.test(input,expect,301))
    def test_var_decl2(self):
        input = "var a: integer;b: real;c: string;"
        expect = str(Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),FloatType()),VarDecl(Id('c'),StringType())]))
        self.assertTrue(TestAST.test(input,expect,302))
    def test_var_decl3(self):
        input = "var _arr: array [1 .. 2] of integer;"
        expect = str(Program([VarDecl(Id('_arr'),ArrayType(1,2,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,303))
    def test_var_decl4(self):
        input = "var _arr: array [1 .. -2] of real;"
        expect = str(Program([VarDecl(Id('_arr'),ArrayType(1,-2,FloatType()))]))
        self.assertTrue(TestAST.test(input,expect,304))
    def test_var_decl5(self):
        input = "var _arr: array [-1 .. 2] of integer;"
        expect = str(Program([VarDecl(Id('_arr'),ArrayType(-1,2,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,305))
    def test_func_decl_1(self):
        input = "function foo():integer;\nbegin\nend"
        expect = str(Program([FuncDecl(Id('foo'),[],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,306))
    def test_func_decl_2(self):
        input = "function foo(a:real):integer;\nbegin\nend"
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),FloatType())],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,307))
    def test_func_decl_3(self):
        input = "function foo(a:real;b:string):array[4 .. 12] of real;\nbegin\nend"
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),FloatType()), VarDecl(Id('b'),StringType())],[],[],ArrayType(4,12,FloatType()))]))
        self.assertTrue(TestAST.test(input,expect,308))
    def test_func_decl_4(self):
        input = "function foo():real;\nvar i,j:integer;\nbegin\nprintln(\"hello\");\nend"
        expect = str(Program([FuncDecl(Id('foo'),[],[VarDecl(Id('i'),IntType()),VarDecl(Id('j'),IntType())],[CallStmt(Id('println'),[StringLiteral('hello')])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,309))
    def test_func_decl_5(self):
        input = "function foo():real;\nvar i,j:integer;k:string;\nbegin\nprintln(\"hello\");\nx:=foo(2)[3];\nend"
        expect = str(Program([FuncDecl(Id('foo'),[],[VarDecl(Id('i'),IntType()),VarDecl(Id('j'),IntType()),VarDecl(Id('k'),StringType())],[CallStmt(Id('println'),[StringLiteral('hello')]),Assign(Id('x'),ArrayCell(CallExpr(Id('foo'),[IntLiteral(2)]),IntLiteral(3)))],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,310))
    def test_proc_decl_1(self):
        input = "procedure foo();begin end"
        expect = str(Program([FuncDecl(Id('foo'),[],[],[])]))
        self.assertTrue(TestAST.test(input,expect,311))
    def test_proc_decl_2(self):
        input = "procedure foo();\nvar x: integer; y: string;\nbegin\nend"
        expect = str(Program([FuncDecl(Id('foo'),[],[VarDecl(Id('x'),IntType()),VarDecl(Id('y'),StringType())],[])]))
        self.assertTrue(TestAST.test(input,expect,312))
    def test_proc_decl_3(self):
        input = "procedure foo();\nbegin\nprint(\"Hello\");\nreturn;\nend"
        expect = str(Program([FuncDecl(Id('foo'),[],[],[CallStmt(Id('print'),[StringLiteral('Hello')]),Return()])]))
        self.assertTrue(TestAST.test(input,expect,313))
    def test_proc_decl_4(self):
        input = "procedure foo(a: integer; b,c: real);\nbegin\nbreak;\nend"
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),IntType()),VarDecl(Id('b'),FloatType()),VarDecl(Id('c'),FloatType())],[],[Break()])]))
        self.assertTrue(TestAST.test(input,expect,314))
    def test_proc_decl_5(self):
        input = "procedure foo();\nbegin\n\nend\nfunction pi(x: real):real;\nbegin\nend"
        expect = str(Program([FuncDecl(Id('foo'),[],[],[]),FuncDecl(Id('pi'),[VarDecl(Id('x'),FloatType())],[],[],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,315))
    def test_assign_1(self):
        input = "procedure main();\nbegin\nx := 1;\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[Assign(Id('x'),IntLiteral(1))])]))
        self.assertTrue(TestAST.test(input,expect,316))
    def test_assign_2(self):
        input = "procedure main();\nbegin\nx:= y:= 1;\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[Assign(Id('y'),IntLiteral(1)),Assign(Id('x'),Id('y'))])]))
        self.assertTrue(TestAST.test(input,expect,317))
    def test_assign_3(self):
        input = "procedure main();\nbegin\na[4]:= 1;\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[Assign(ArrayCell(Id('a'),IntLiteral(4)),IntLiteral(1))])]))
        self.assertTrue(TestAST.test(input,expect,318))
    def test_assign_4(self):
        input = "procedure main();\nbegin\nx:=c[x+2] := 2;\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[Assign(ArrayCell(Id('c'),BinaryOp('+',Id('x'),IntLiteral(2))),IntLiteral(2)),Assign(Id('x'),ArrayCell(Id('c'),BinaryOp('+',Id('x'),IntLiteral(2))))])]))
        self.assertTrue(TestAST.test(input,expect,319))
    def test_assign_5(self):
        input = "procedure main();\nbegin\nfoo(1,a)[1]:= y := 2;\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[Assign(Id('y'),IntLiteral(2)),Assign(ArrayCell(CallExpr(Id('foo'),[IntLiteral(1),Id('a')]),IntLiteral(1)),Id('y'))])]))
        self.assertTrue(TestAST.test(input,expect,320))
    def test_assign_6(self):
        input = "procedure main();\nbegin\nx:=y:=foo[(x+2)*2];\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[Assign(Id('y'),ArrayCell(Id('foo'),BinaryOp('*',BinaryOp('+',Id('x'),IntLiteral(2)),IntLiteral(2)))),Assign(Id('x'),Id('y'))])]))
        self.assertTrue(TestAST.test(input,expect,321))
    def test_assign_7(self):
        input = "procedure main();\nbegin\nx:=foo()[1]:=4;\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[Assign(ArrayCell(CallExpr(Id('foo'),[]),IntLiteral(1)),IntLiteral(4)),Assign(Id('x'),ArrayCell(CallExpr(Id('foo'),[]),IntLiteral(1)))])]))
        self.assertTrue(TestAST.test(input,expect,322))
    def test_assign_8(self):
        input = "procedure main();\nbegin\nx:= \"hello\";\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[Assign(Id('x'),StringLiteral('hello'))])]))
        self.assertTrue(TestAST.test(input,expect,323))
    def test_assign_9(self):
        input = "procedure main();\nbegin\nx:= 1;\ny:=1+2-foo();\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[Assign(Id('x'),IntLiteral(1)),Assign(Id('y'),BinaryOp('-',BinaryOp('+',IntLiteral(1),IntLiteral(2)),CallExpr(Id('foo'),[])))])]))
        self.assertTrue(TestAST.test(input,expect,324))
    def test_assign_10(self):
        input = "procedure main();\nbegin\nx:= a[b+c[4/x]];\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[Assign(Id('x'),ArrayCell(Id('a'),BinaryOp('+',Id('b'),ArrayCell(Id('c'),BinaryOp('/',IntLiteral(4),Id('x'))))))])]))
        self.assertTrue(TestAST.test(input,expect,325))
    def test_if_1(self):
        input = "procedure main();\nbegin\nif(a<2)then\na:=a+1;\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[If(BinaryOp('<',Id('a'),IntLiteral(2)),[Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral(1)))])])]))
        self.assertTrue(TestAST.test(input,expect,326))
    def test_if_2(self):
        input = "procedure main();\nbegin\nif(tRuE)then\nreturn false;\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[If(BooleanLiteral(True),[Return(BooleanLiteral(False))])])]))
        self.assertTrue(TestAST.test(input,expect,327))
    def test_if_3(self):
        input = "procedure main();\nbegin\nif(x=2)then\nbegin\nx:=x+1;\nfoo();\nend\nelse\nx:=x-1;\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[If(BinaryOp('=',Id('x'),IntLiteral(2)),[Assign(Id('x'),BinaryOp('+',Id('x'),IntLiteral(1))),CallStmt(Id('foo'),[])],[Assign(Id('x'),BinaryOp('-',Id('x'),IntLiteral(1)))])])]))
        self.assertTrue(TestAST.test(input,expect,328))
    def test_if_4(self):
        input = "procedure main();\nbegin\nif(x=2)then\nif(y<>2)then\nfoo();\nelse\nprint(\"lmao\");\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[If(BinaryOp('=',Id('x'),IntLiteral(2)),[If(BinaryOp('<>',Id('y'),IntLiteral(2)),[CallStmt(Id('foo'),[])],[CallStmt(Id('print'),[StringLiteral('lmao')])])])])]))
        self.assertTrue(TestAST.test(input,expect,329))
    def test_if_5(self):
        input = "procedure main();\nbegin\nif(x=2)then\nx:=x+1;\nelse if(x<2)then\nx:=x-1;\nelse\nprint(\"lul\");\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[If(BinaryOp('=',Id('x'),IntLiteral(2)),[Assign(Id('x'),BinaryOp('+',Id('x'),IntLiteral(1)))],[If(BinaryOp('<',Id('x'),IntLiteral(2)),[Assign(Id('x'),BinaryOp('-',Id('x'),IntLiteral(1)))],[CallStmt(Id('print'),[StringLiteral('lul')])])])])]))
        self.assertTrue(TestAST.test(input,expect,330))
    def test_if_6(self):
        input = "procedure main();\nbegin\nif(a)then\ny:=foo(x-b/2,1);\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[If(Id('a'),[Assign(Id('y'),CallExpr(Id('foo'),[BinaryOp('-',Id('x'),BinaryOp('/',Id('b'),IntLiteral(2))),IntLiteral(1)]))],[])])]))
        self.assertTrue(TestAST.test(input,expect,331))
    def test_if_7(self):
        input = "procedure main();\nbegin\nif(a = false)then\nbegin\ny:=foo(2)[3 DIV x];\nend\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[If(BinaryOp('=',Id('a'),BooleanLiteral(False)),[Assign(Id('y'),ArrayCell(CallExpr(Id('foo'),[IntLiteral(2)]),BinaryOp('DIV',IntLiteral(3),Id('x'))))],[])])]))
        self.assertTrue(TestAST.test(input,expect,332))
    def test_if_8(self):
        input = "procedure main();\nbegin\nif(a = true)then\nbegin\ny:=foo(2)[3 DIV x];\nend\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[If(BinaryOp('=',Id('a'),BooleanLiteral(True)),[Assign(Id('y'),ArrayCell(CallExpr(Id('foo'),[IntLiteral(2)]),BinaryOp('DIV',IntLiteral(3),Id('x'))))],[])])]))
        self.assertTrue(TestAST.test(input,expect,333))
    def test_if_9(self):
        input = "procedure main();\nbegin\nif(a=b)then\na:=a+b;\nelse if(a<b)then\nbegin\na:=a+1;\nprintln(a);\nend\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[If(BinaryOp('=',Id('a'),Id('b')),[Assign(Id('a'),BinaryOp('+',Id('a'),Id('b')))],[If(BinaryOp('<',Id('a'),Id('b')),[Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral(1))),CallStmt(Id('println'),[Id('a')])],[])])])]))
        self.assertTrue(TestAST.test(input,expect,334))
    def test_if_10(self):
        input = "procedure main();\nbegin\nif(a=b)then\nif(c=d)then\nprintln(\"hello\");\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[If(BinaryOp('=',Id('a'),Id('b')),[If(BinaryOp('=',Id('c'),Id('d')),[CallStmt(Id('println'),[StringLiteral('hello')])],[])],[])])]))
        self.assertTrue(TestAST.test(input,expect,335))
    def test_loop_1(self):
        input = "procedure main();\nbegin\nfor i:=1 to 5 do\nprintln(\"hello\");\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[For(Id('i'),IntLiteral(1),IntLiteral(5),True,[CallStmt(Id('println'),[StringLiteral('hello')])])])]))
        self.assertTrue(TestAST.test(input,expect,336))
    def test_loop_2(self):
        input = "procedure main();\nbegin\nfor i:=5 downto (-4/4*-1) do\nx:=foo()[2];\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[For(Id('i'),IntLiteral(5),BinaryOp('*',BinaryOp('/',UnaryOp('-',IntLiteral(4)),IntLiteral(4)),UnaryOp('-',IntLiteral(1))),False,[Assign(Id('x'),ArrayCell(CallExpr(Id('foo'),[]),IntLiteral(2)))])])]))
        self.assertTrue(TestAST.test(input,expect,337))
    def test_loop_3(self):
        input = "procedure main();\nbegin\nfor i:=foo(2) to false do\nprintln(\"he\\tllo\");\nif(true)then\nbreak;\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[For(Id('i'),CallExpr(Id('foo'),[IntLiteral(2)]),BooleanLiteral(False),True,[CallStmt(Id('println'),[StringLiteral('he\\tllo')])]),If(BooleanLiteral(True),[Break()],[])])]))
        self.assertTrue(TestAST.test(input,expect,338))
    def test_loop_4(self):
        input = "procedure main();\nbegin\nfor i:=a to b do\nbegin\nfor j:=0 downto -2 do\nprintln(i=j);\nend\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[For(Id('i'),Id('a'),Id('b'),True,[For(Id('j'),IntLiteral(0),UnaryOp('-',IntLiteral(2)),False,[CallStmt(Id('println'),[BinaryOp('=',Id('i'),Id('j'))])])])])]))
        self.assertTrue(TestAST.test(input,expect,339))
    def test_loop_5(self):
        input = "procedure main();\nvar a: integer;b: real;\nbegin\nfor i:=1 to 5 do\nbegin\na:=2;\nb:=a/2+a*(a>4-1);\nif(false)then\ncontinue;\nend\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[VarDecl(Id('a'),IntType()),VarDecl(Id('b'),FloatType())],[For(Id('i'),IntLiteral(1),IntLiteral(5),True,[Assign(Id('a'),IntLiteral(2)),Assign(Id('b'),BinaryOp('+',BinaryOp('/',Id('a'),IntLiteral(2)),BinaryOp('*',Id('a'),BinaryOp('>',Id('a'),BinaryOp('-',IntLiteral(4),IntLiteral(1)))))),If(BooleanLiteral(False),[Continue()],[])])])]))
        self.assertTrue(TestAST.test(input,expect,340))
    def test_loop_6(self):
        input = "procedure main();\nvar i:integer;\nbegin\ni:=0;\nwhile (i<5) do\nprintln(\"hello\");\ni:=i+1;\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[VarDecl(Id('i'),IntType())],[Assign(Id('i'),IntLiteral(0)),While(BinaryOp('<',Id('i'),IntLiteral(5)),[CallStmt(Id('println'),[StringLiteral('hello')])]),Assign(Id('i'),BinaryOp('+',Id('i'),IntLiteral(1)))])]))
        self.assertTrue(TestAST.test(input,expect,341))
    def test_loop_7(self):
        input = "procedure main();\nvar i:integer;\nbegin\ni:=0;\nwhile (i>-5) do\nfor j:=0 downto -2 do\nprintln(\"hello\");\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[VarDecl(Id('i'),IntType())],[Assign(Id('i'),IntLiteral(0)),While(BinaryOp('>',Id('i'),UnaryOp('-',IntLiteral(5))),[For(Id('j'),IntLiteral(0),UnaryOp('-',IntLiteral(2)),False,[CallStmt(Id('println'),[StringLiteral('hello')])])])])]))
        self.assertTrue(TestAST.test(input,expect,342))
    def test_loop_8(self):
        input = "procedure main();\nvar i:integer;\nbegin\ni:=0;\nwhile (x) do\nprintln(x);\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[VarDecl(Id('i'),IntType())],[Assign(Id('i'),IntLiteral(0)),While(Id('x'),[CallStmt(Id('println'),[Id('x')])])])]))
        self.assertTrue(TestAST.test(input,expect,343))
    def test_loop_9(self):
        input = "procedure main();\nvar i:integer;\nbegin\ni:=0;\nwhile (i<5) do\nprintln(\"hello\\ntabc\",0.5);\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[VarDecl(Id('i'),IntType())],[Assign(Id('i'),IntLiteral(0)),While(BinaryOp('<',Id('i'),IntLiteral(5)),[CallStmt(Id('println'),[StringLiteral('hello\\ntabc'),FloatLiteral(0.5)])])])]))
        self.assertTrue(TestAST.test(input,expect,344))
    def test_loop_10(self):
        input = "procedure main();\nvar i:integer;\nbegin\ni:=0;\nwhile (i<5) do\nwhile (j>5) do\nexit();\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[VarDecl(Id('i'),IntType())],[Assign(Id('i'),IntLiteral(0)),While(BinaryOp('<',Id('i'),IntLiteral(5)),[While(BinaryOp('>',Id('j'),IntLiteral(5)),[CallStmt(Id('exit'),[])])])])]))
        self.assertTrue(TestAST.test(input,expect,345))
    def test_with_1(self):
        input = "procedure main();\nbegin\nwith a,b:integer;c:array[1 .. 2]of real; do\nd:=c[a]+b;\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[With([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),ArrayType(1,2,FloatType()))],[Assign(Id('d'),BinaryOp('+',ArrayCell(Id('c'),Id('a')),Id('b')))])])]))
        self.assertTrue(TestAST.test(input,expect,346))
    def test_with_2(self):
        input = "procedure main();\nbegin\nwith a,b:integer;c:array[-1 .. 2]of real; do\nif(a<b)then\nc[a]:=c[b];\n\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[With([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),ArrayType(-1,2,FloatType()))],[If(BinaryOp('<',Id('a'),Id('b')),[Assign(ArrayCell(Id('c'),Id('a')),ArrayCell(Id('c'),Id('b')))],[])])])]))
        self.assertTrue(TestAST.test(input,expect,347))
    def test_with_3(self):
        input = "procedure main();\nbegin\nwith a,b:integer;c:array[1 .. 2]of real; do\nbegin\nprintln(\"hello\");\nd:=c[a]+b;\nend\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[With([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),ArrayType(1,2,FloatType()))],[CallStmt(Id('println'),[StringLiteral('hello')]),Assign(Id('d'),BinaryOp('+',ArrayCell(Id('c'),Id('a')),Id('b')))])])]))
        self.assertTrue(TestAST.test(input,expect,348))
    def test_with_4(self):
        input = "procedure main();\nbegin\nwith a,b: string; do\nwith c: array [1 .. 2]of real;do\nd:=c[a]+b;\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[With([VarDecl(Id('a'),StringType()),VarDecl(Id('b'),StringType())],[With([VarDecl(Id('c'),ArrayType(1,2,FloatType()))],[Assign(Id('d'),BinaryOp('+',ArrayCell(Id('c'),Id('a')),Id('b')))])])])]))
        self.assertTrue(TestAST.test(input,expect,349))
    def test_with_5(self):
        input = "procedure main();\nbegin\nwith a,b:integer;c:array[1 .. 2]of real; do\nif(a<b)then\nc[a]:=c[b];\n\nend"
        expect = str(Program([FuncDecl(Id('main'),[],[],[With([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),ArrayType(1,2,FloatType()))],[If(BinaryOp('<',Id('a'),Id('b')),[Assign(ArrayCell(Id('c'),Id('a')),ArrayCell(Id('c'),Id('b')))],[])])])]))
        self.assertTrue(TestAST.test(input,expect,350))
    def test_exp_1(self):
        input = "PROCEDURE MAIN();\nbegin\na:= a[b-2+foo()[5]];\nEND"
        expect = str(Program([FuncDecl(Id('MAIN'),[],[],[Assign(Id('a'),ArrayCell(Id('a'),BinaryOp('+',BinaryOp('-',Id('b'),IntLiteral(2)),ArrayCell(CallExpr(Id('foo'),[]),IntLiteral(5)))))])]))
        self.assertTrue(TestAST.test(input,expect,351))
    def test_exp_2(self):
        input = "PROCEDURE main();\nbegin\na := a[b-2+foo(b,c/5)[5]];\nEND"
        expect = str(Program([FuncDecl(Id('main'),[],[],[Assign(Id('a'),ArrayCell(Id('a'),BinaryOp('+',BinaryOp('-',Id('b'),IntLiteral(2)),ArrayCell(CallExpr(Id('foo'),[Id('b'),BinaryOp('/',Id('c'),IntLiteral(5))]),IntLiteral(5)))))])]))
        self.assertTrue(TestAST.test(input,expect,352))
    def test_exp_3(self):
        input = "PROCEDURE main();\nbegin\nx:= a[foo(2)+b[-5-goo()[1]]];\nEND"
        expect = str(Program([FuncDecl(Id('main'),[],[],[Assign(Id('x'),ArrayCell(Id('a'),BinaryOp('+',CallExpr(Id('foo'),[IntLiteral(2)]),ArrayCell(Id('b'),BinaryOp('-',UnaryOp('-',IntLiteral(5)),ArrayCell(CallExpr(Id('goo'),[]),IntLiteral(1)))))))])]))
        self.assertTrue(TestAST.test(input,expect,353))
    def test_exp_4(self):
        input = "PROCEDURE main();\nbegin\nfoo(hoo(5)[2-x]);\nEND"
        expect = str(Program([FuncDecl(Id('main'),[],[],[CallStmt(Id('foo'),[ArrayCell(CallExpr(Id('hoo'),[IntLiteral(5)]),BinaryOp('-',IntLiteral(2),Id('x')))])])]))
        self.assertTrue(TestAST.test(input,expect,354))
    def test_exp_5(self):
        input = "PROCEDURE main();\nbegin\nx := 2 + 1[1];\nEND"
        expect = str(Program([FuncDecl(Id('main'),[],[],[Assign(Id('x'),BinaryOp('+',IntLiteral(2),ArrayCell(IntLiteral(1),IntLiteral(1))))])]))
        self.assertTrue(TestAST.test(input,expect,355))
    def test_exp_6(self):
        input = "PROCEDURE main();\nbegin\nreturn a and then not b or else not a and b;\nEnd"
        expect = str(Program([FuncDecl(Id('main'),[],[],[Return(BinaryOp('orelse',BinaryOp('andthen',Id('a'),UnaryOp('not',Id('b'))),BinaryOp('and',UnaryOp('not',Id('a')),Id('b'))))])]))
        self.assertTrue(TestAST.test(input,expect,356))
    def test_exp_7(self):
        input = "PROCEDURE main();\nbegin\na := b[c[d[e]]];\nEND"
        expect = str(Program([FuncDecl(Id('main'),[],[],[Assign(Id('a'),ArrayCell(Id('b'),ArrayCell(Id('c'),ArrayCell(Id('d'),Id('e')))))])]))
        self.assertTrue(TestAST.test(input,expect,357))
    def test_exp_8(self):
        input = "PROCEDURE quad(a,b,c: integer);\nvar delta: real;\nbegin\ndelta := b*b-4*a*c;\nroot_1:=-b + sqrt(delta);\nEND"
        expect = str(Program([FuncDecl(Id('quad'),[VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType())],[VarDecl(Id('delta'),FloatType())],[Assign(Id('delta'),BinaryOp('-',BinaryOp('*',Id('b'),Id('b')),BinaryOp('*',BinaryOp('*',IntLiteral(4),Id('a')),Id('c')))),Assign(Id('root_1'),BinaryOp('+',UnaryOp('-',Id('b')),CallExpr(Id('sqrt'),[Id('delta')])))])]))
        self.assertTrue(TestAST.test(input,expect,358))
    def test_exp_9(self):
        input = "PROCEDURE main();\nbegin\nreturn a < b;\nEND"
        expect = str(Program([FuncDecl(Id('main'),[],[],[Return(BinaryOp('<',Id('a'),Id('b')))])]))
        self.assertTrue(TestAST.test(input,expect,359))
    def test_exp_10(self):
        input = "PROCEDURE main();\nbegin\nreturn (a < b) <> (c > d);\nEND"
        expect = str(Program([FuncDecl(Id('main'),[],[],[Return(BinaryOp('<>',BinaryOp('<',Id('a'),Id('b')),BinaryOp('>',Id('c'),Id('d'))))])]))
        self.assertTrue(TestAST.test(input,expect,360))
    def test_cmplx_prog_1(self):
        input = """ Function sort(arr: array[1 .. 200] of integer):array[1 .. 200] of integer;
                    VAR i,j,k: integer;
                    begin
                        for i:=2 to 20 do
                        begin
                            k:=arr[i];
                        end
                        j := j-1;
                        return arr;
                    end
                """
        expect = str(Program([FuncDecl(Id('sort'),
                    [VarDecl(Id('arr'),ArrayType(1,200,IntType()))],
                    [VarDecl(Id('i'),IntType()),VarDecl(Id('j'),IntType()),VarDecl(Id('k'),IntType())],
                    [For(Id('i'),IntLiteral(2),IntLiteral(20),True,
                        [Assign(Id('k'),ArrayCell(Id('arr'),Id('i')))]),
                    Assign(Id('j'),BinaryOp('-',Id('j'),IntLiteral(1))),
                    Return(Id('arr'))],
                    ArrayType(1,200,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,361))
    def test_cmplx_prog_2(self):
        input = """ var i: integer;
                    procedure foo(x: integer);
                    begin
                        x:=i;
                    end
                    function goo():integer;
                    begin
                        return rand(i,seed);
                    end """
        expect = str(Program([VarDecl(Id('i'),IntType()),
                    FuncDecl(Id('foo'),
                    [VarDecl(Id('x'),IntType())],
                    [],
                    [Assign(Id('x'),Id('i'))]),
                    FuncDecl(Id('goo'),
                    [],
                    [],
                    [Return(CallExpr(Id('rand'),[Id('i'),Id('seed')]))],
                    IntType())]))
        self.assertTrue(TestAST.test(input,expect,362))
    def test_cmplx_prog_3(self):
        input = """ Function fib(n:integer):integer;
                    begin
                        if (n = 0) or (n = 1) then return 1;
                        else return fib(n-1)+fib(n-2);
                    end """
        expect = str(Program([FuncDecl(Id('fib'),
                    [VarDecl(Id('n'),IntType())],
                    [],
                    [If(BinaryOp('or',BinaryOp('=',Id('n'),IntLiteral(0)),BinaryOp('=',Id('n'),IntLiteral(1))),
                        [Return(IntLiteral(1))],
                        [Return(BinaryOp('+',CallExpr(Id('fib'),[BinaryOp('-',Id('n'),IntLiteral(1))]),CallExpr(Id('fib'),[BinaryOp('-',Id('n'),IntLiteral(2))])))])],
                    IntType())]))
        self.assertTrue(TestAST.test(input,expect,363))
    def test_cmplx_prog_4(self):
        input = """ Function sin(x,e:real):real;
                    Var result,elm:real;
                    begin
                        err:=x;
                        while (elm>e) do
                        begin
                            result:=result+elm;
                            elm:=elm*(-sqr(x)/e);
                        end
                        return result;
                    end """
        expect = str(Program([FuncDecl(Id('sin'),
                    [VarDecl(Id('x'),FloatType()),VarDecl(Id('e'),FloatType())],
                    [VarDecl(Id('result'),FloatType()),VarDecl(Id('elm'),FloatType())],
                    [Assign(Id('err'),Id('x')),
                    While(BinaryOp('>',Id('elm'),Id('e')),
                          [Assign(Id('result'),BinaryOp('+',Id('result'),Id('elm'))),
                          Assign(Id('elm'),BinaryOp('*',Id('elm'),BinaryOp('/',UnaryOp('-',CallExpr(Id('sqr'),[Id('x')])),Id('e'))))]),
                    Return(Id('result'))],
                    FloatType())]))
        self.assertTrue(TestAST.test(input,expect,364))
    def test_cmplx_prog_5(self):
        input = """ Function exp(x:real):real;
                    VAR result:real;
                    begin
                        if (x<0) then
                        begin
                            printLn("no negative!");
                            return;
                        end
                        return pow(e,x);
                    end """
        expect = str(Program([FuncDecl(Id('exp'),
                    [VarDecl(Id('x'),FloatType())],
                    [VarDecl(Id('result'),FloatType())],
                    [If(BinaryOp('<',Id('x'),IntLiteral(0)),
                        [CallStmt(Id('printLn'),[StringLiteral('no negative!')]),
                        Return()],
                        []),
                    Return(CallExpr(Id('pow'),[Id('e'),Id('x')]))],
                    FloatType())]))
        self.assertTrue(TestAST.test(input,expect,365))
    def test_cmplx_prog_6(self):
        input = """ procedure main();
                    begin
                        println("hello");
                        if (f(a,b) = f(b,a)) then
                            return toString(func(f));
                        else return exception(invalidFunc);
                    end
                """
        expect = str(Program([FuncDecl(Id('main'),
                    [],
                    [],
                    [CallStmt(Id('println'),[StringLiteral('hello')]),
                    If(BinaryOp('=',CallExpr(Id('f'),[Id('a'),Id('b')]),CallExpr(Id('f'),[Id('b'),Id('a')])),
                        [Return(CallExpr(Id('toString'),[CallExpr(Id('func'),[Id('f')])]))],
                        [Return(CallExpr(Id('exception'),[Id('invalidFunc')]))])]
                    )]))
        self.assertTrue(TestAST.test(input,expect,366))
    def test_cmplx_prog_7(self):
        input = """ procedure main();
                    begin
                        while true do
                            return (x<>1);
                    end
                """
        expect = str(Program([FuncDecl(Id('main'),
                    [],
                    [],
                    [While(BooleanLiteral(True),
                           [Return(BinaryOp('<>',Id('x'),IntLiteral(1)))])]
                    )]))
        self.assertTrue(TestAST.test(input,expect,367))
    def test_cmplx_prog_8(self):
        input = """ function foo(a:array[1 .. 20] of integer):array[1 .. 20] of integer;
                    var i,j,x,m: integer;
                    begin
                        for i:=1 to 19 do
                        begin
                            x:=1;
                            for j:=i+1 to 20 do
                                if (a[j]<a[m]) then m:=j;
                            if (m <> 1) then swap(a[i],a[m]);
                        end
                    end
                """
        expect = str(Program([FuncDecl(Id('foo'),
                    [VarDecl(Id('a'),ArrayType(1,20,IntType()))],
                    [VarDecl(Id('i'),IntType()),VarDecl(Id('j'),IntType()),VarDecl(Id('x'),IntType()),VarDecl(Id('m'),IntType())],
                    [For(Id('i'),
                        IntLiteral(1),
                        IntLiteral(19),
                        True,
                        [Assign(Id('x'),IntLiteral(1)),
                        For(Id('j'),
                            BinaryOp('+',Id('i'),IntLiteral(1)),
                            IntLiteral(20),
                            True,
                            [If(BinaryOp('<',ArrayCell(Id('a'),Id('j')),ArrayCell(Id('a'),Id('m'))),
                                [Assign(Id('m'),Id('j'))])]),
                        If(BinaryOp('<>',Id('m'),IntLiteral(1)),
                                [CallStmt(Id('swap'),
                                          [ArrayCell(Id('a'),Id('i')),
                                          ArrayCell(Id('a'),Id('m'))])])])],
                    ArrayType(1,20,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,368))
    def test_cmplx_prog_9(self):
        input = """ function find(a: array[1 .. 20] of integer;target:integer):boolean;
                    var hi,lo,m : integer;
                    begin
                        lo:=1;hi:=20;
                        while(lo<hi) do
                        begin
                            m:=(hi+lo) div 2;
                            if (a[m]<target) then lo:=m+1;
                            else if (a[m]>target) then hi:=m-1;
                            else return true;
                        end
                        return false;
                    end
                """
        expect = str(Program([FuncDecl(Id('find'),
                    [VarDecl(Id('a'),ArrayType(1,20,IntType())),
                    VarDecl(Id('target'),IntType())],
                    [VarDecl(Id('hi'),IntType()),VarDecl(Id('lo'),IntType()),VarDecl(Id('m'),IntType())],
                    [Assign(Id('lo'),IntLiteral(1)),
                    Assign(Id('hi'),IntLiteral(20)),
                    While(BinaryOp('<',Id('lo'),Id('hi')),
                          [Assign(Id('m'),
                                  BinaryOp('div',BinaryOp('+',Id('hi'),Id('lo')),IntLiteral(2))),
                          If(BinaryOp('<',ArrayCell(Id('a'),Id('m')),Id('target')),
                            [Assign(Id('lo'),BinaryOp('+',Id('m'),IntLiteral(1)))],
                            [If(BinaryOp('>',ArrayCell(Id('a'),Id('m')),Id('target')),
                                [Assign(Id('hi'),BinaryOp('-',Id('m'),IntLiteral(1)))],
                                [Return(BooleanLiteral(True))])])]),
                    Return(BooleanLiteral(False))],
                    BoolType())]))
        self.assertTrue(TestAST.test(input,expect,369))
    def test_cmplx_prog_10(self):
        input = """ procedure main();
                    begin
                        println("Enter a: ");
                        readLn();
                        println("Enter b: ");
                        readLn();
                        println("Sum is: ",a+b);
                    end
                """
        expect = str(Program([FuncDecl(Id('main'),
                    [],
                    [],
                    [CallStmt(Id('println'),[StringLiteral('Enter a: ')]),
                     CallStmt(Id('readLn'),[]),
                     CallStmt(Id('println'),[StringLiteral('Enter b: ')]),
                     CallStmt(Id('readLn'),[]),
                     CallStmt(Id('println'),[StringLiteral('Sum is: '),BinaryOp('+',Id('a'),Id('b'))])]
                    )]))
        self.assertTrue(TestAST.test(input,expect,370))
    def test_cmplx_prog_11(self):
        input = """ Procedure DisPosePointer();
                    Begin
                        i:=1;
                        while i<=10 do
                            release(contour);
                        dispose(contour);
                    End
                """
        expect = str(Program([FuncDecl(Id('DisPosePointer'),
                    [],
                    [],
                    [Assign(Id('i'),IntLiteral(1)),
                    While(BinaryOp('<=',Id('i'),IntLiteral(10)),
                          [CallStmt(Id('release'),[Id('contour')])]),
                    CallStmt(Id('dispose'),[Id('contour')])]
                    )]))
        self.assertTrue(TestAST.test(input,expect,371))
    def test_cmplx_prog_12(self):
        input = """ Procedure VerifyChrono();
                    Var h,m,s:integer;
                    Begin
                        if s<0 then begin
                            s:=60+s;m:=m-1;
                        end
                        Bar(261,1,279+TextWidth("00")+20,24);
                        Str(s,Sec);
                        SetWriteMode(1);
                    End
                """
        expect = str(Program([FuncDecl(Id('VerifyChrono'),
                    [],
                    [VarDecl(Id('h'),IntType()),VarDecl(Id('m'),IntType()),VarDecl(Id('s'),IntType())],
                    [If(BinaryOp('<',Id('s'),IntLiteral(0)),
                        [Assign(Id('s'),BinaryOp('+',IntLiteral(60),Id('s'))),
                        Assign(Id('m'),BinaryOp('-',Id('m'),IntLiteral(1)))],
                        []),
                    CallStmt(Id('Bar'),[IntLiteral(261),
                                        IntLiteral(1),
                                        BinaryOp('+',BinaryOp('+',IntLiteral(279),CallExpr(Id('TextWidth'),
                                                                                            [StringLiteral('00')])),
                                                    IntLiteral(20)),
                                        IntLiteral(24)]),
                    CallStmt(Id('Str'),[Id('s'),Id('Sec')]),
                    CallStmt(Id('SetWriteMode'),[IntLiteral(1)])]
                    )]))
        self.assertTrue(TestAST.test(input,expect,372))
    def test_cmplx_prog_13(self):
        input = """ Procedure Titre();
                    Begin
                        i:=i+1;
                        if i=16 then i:=1;
                        SetColor(i);
                        OutTextXY(GetMaxX DIV 2,170,"Think WAY");
                    End
                """
        expect = str(Program([FuncDecl(Id('Titre'),
                    [],
                    [],
                    [Assign(Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
                    If(BinaryOp('=',Id('i'),IntLiteral(16)),
                       [Assign(Id('i'),IntLiteral(1))]),
                    CallStmt(Id('SetColor'),[Id('i')]),
                    CallStmt(Id('OutTextXY'),[BinaryOp('DIV',Id('GetMaxX'),IntLiteral(2)),
                                              IntLiteral(170),
                                              StringLiteral('Think WAY')])]
                    )]))
        self.assertTrue(TestAST.test(input,expect,373))
    def test_cmplx_prog_14(self):
        input = """ procedure vide_buffer();
                    begin
                        ax:="0c0B";
                        intr(21,r);
                    end
                    
                    procedure Verify();
                    begin
                        if CodeErreur <> grOK then
                        begin
                            CloseGraph();
                            WriteLn("Erreur graphique: ");
                            Halt(1);
                        end
                    end
                """
        expect = str(Program([FuncDecl(Id('vide_buffer'),
                    [],
                    [],
                    [Assign(Id('ax'),StringLiteral('0c0B')),
                    CallStmt(Id('intr'),[IntLiteral(21),Id('r')])]
                    ),
                    FuncDecl(Id('Verify'),
                    [],
                    [],
                    [If(BinaryOp('<>',Id('CodeErreur'),Id('grOK')),
                        [CallStmt(Id('CloseGraph'),[]),
                        CallStmt(Id('WriteLn'),[StringLiteral('Erreur graphique: ')]),
                        CallStmt(Id('Halt'),[IntLiteral(1)])],
                        [])])]))
        self.assertTrue(TestAST.test(input,expect,374))
    def test_cmplx_prog_15(self):
        input = """ procedure litcar(ch:String);
                    begin
                        ch:=readKey;
                        if (ch=0) then ch:=chr(ord(readkey)+128);
                        ch:=upcase(ch);
                    end
                """
        expect = str(Program([FuncDecl(Id('litcar'),
                    [VarDecl(Id('ch'),StringType())],
                    [],
                    [Assign(Id('ch'),Id('readKey')),
                    If(BinaryOp('=',Id('ch'),IntLiteral(0)),
                       [Assign(Id('ch'),
                               CallExpr(Id('chr'),[BinaryOp('+',CallExpr(Id('ord'),[Id('readkey')]),
                                                            IntLiteral(128))]))],
                       []),
                    Assign(Id('ch'),CallExpr(Id('upcase'),[Id('ch')]))]
                    )]))
        self.assertTrue(TestAST.test(input,expect,375))
    def test_cmplx_prog_16(self):
        input = """ Function Securit():boolean;
                    begin
                        Entete("Etes-vous s-r?",true);
                        ChoixDansMenu("Oui, Non",a["O"],"ON",60.e6,25,ch);
                        Securit:=(ch="O");
                    end
                """
        expect = str(Program([FuncDecl(Id('Securit'),
                    [],
                    [],
                    [CallStmt(Id('Entete'),[StringLiteral('Etes-vous s-r?'),BooleanLiteral(True)]),
                    CallStmt(Id('ChoixDansMenu'),[StringLiteral('Oui, Non'),
                                                  ArrayCell(Id('a'),StringLiteral('O')),
                                                  StringLiteral('ON'),
                                                  FloatLiteral(60.e6),
                                                  IntLiteral(25),
                                                  Id('ch')]),
                    Assign(Id('Securit'),BinaryOp('=',Id('ch'),StringLiteral('O')))]
                    ,BoolType())]))
        self.assertTrue(TestAST.test(input,expect,376))
    def test_cmplx_prog_17(self):
        input = """ Procedure Ecris(Texte:String;error:boolean);
                    begin
                        setcolor(1);
                        ligne:=ligne+1;
                        error:=true;
                        if ligne=24 then
                        begin
                            sound(780);Delay(200);Nosound();
                            ligne:=3;
                        end
                        outtextXY(340,8*ligne,texte);
                    end
                """
        expect = str(Program([FuncDecl(Id('Ecris'),
                    [VarDecl(Id('Texte'),StringType()),VarDecl(Id('error'),BoolType())],
                    [],
                    [CallStmt(Id('setcolor'),[IntLiteral(1)]),
                    Assign(Id('ligne'),BinaryOp('+',Id('ligne'),IntLiteral(1))),
                    Assign(Id('error'),BooleanLiteral(True)),
                    If(BinaryOp('=',Id('ligne'),IntLiteral(24)),
                       [CallStmt(Id('sound'),[IntLiteral(780)]),
                       CallStmt(Id('Delay'),[IntLiteral(200)]),
                       CallStmt(Id('Nosound'),[]),
                       Assign(Id('ligne'),IntLiteral(3))],
                       []),
                    CallStmt(Id('outtextXY'),[IntLiteral(340),
                                              BinaryOp('*',IntLiteral(8),Id('ligne')),
                                              Id('texte')])]
                    )]))
        self.assertTrue(TestAST.test(input,expect,377))
    def test_cmplx_prog_18(self):
        input = """ function CaseCoul(i,j:integer): real;
                    var m: integer;
                    begin
                        m:=i+j;
                        if m MOD 2=0 then CaseCaul:=1;
                        else CaseCoul:=0;
                    end
                """
        expect = str(Program([FuncDecl(Id('CaseCoul'),
                    [VarDecl(Id('i'),IntType()),VarDecl(Id('j'),IntType())],
                    [VarDecl(Id('m'),IntType())],
                    [Assign(Id('m'),BinaryOp('+',Id('i'),Id('j'))),
                    If(BinaryOp('=',BinaryOp('MOD',Id('m'),IntLiteral(2)),IntLiteral(0)),
                       [Assign(Id('CaseCaul'),IntLiteral(1))],
                       [Assign(Id('CaseCoul'),IntLiteral(0))])]
                    ,FloatType())]))
        self.assertTrue(TestAST.test(input,expect,378))
    def test_cmplx_prog_19(self):
        input = """ procedure Zone(x,y,long,larg:integer;p:real);
                    Begin
                        GetMem(P,ImageSize(x,y,x+long,y+larg));
                        GetImage(x,y);
                    End
                    
                    Procedure Entete(Texte:String;eff:Boolean);
                    begin
                        If eff Then begin
                            SetColor(0);
                            Bar(0,0,GetMaxX,17);
                        end
                    end
                """
        expect = str(Program([FuncDecl(Id('Zone'),
                    [VarDecl(Id('x'),IntType()),VarDecl(Id('y'),IntType()),
                    VarDecl(Id('long'),IntType()),VarDecl(Id('larg'),IntType()),
                    VarDecl(Id('p'),FloatType())],
                    [],
                    [CallStmt(Id('GetMem'),[Id('P'),CallExpr(Id('ImageSize'),[Id('x'),
                                                                              Id('y'),
                                                                              BinaryOp('+',Id('x'),Id('long')),
                                                                              BinaryOp('+',Id('y'),Id('larg'))])]),
                    CallStmt(Id('GetImage'),[Id('x'),Id('y')])]
                    ),FuncDecl(Id('Entete'),
                    [VarDecl(Id('Texte'),StringType()),VarDecl(Id('eff'),BoolType())],
                    [],
                    [If(Id('eff'),
                        [CallStmt(Id('SetColor'),[IntLiteral(0)]),
                        CallStmt(Id('Bar'),[IntLiteral(0),IntLiteral(0),Id('GetMaxX'),IntLiteral(17)])],
                        [])])]))
        self.assertTrue(TestAST.test(input,expect,379))
    def test_cmplx_prog_20(self):
        input = """ procedure afficherfleche(x1,x2,y1,y2:integer;allume:boolean);
                    var cob:real;poly:array[1 .. 3] of integer;
                    begin
                        if allume then cob:=2; else cob:=1;
                        setfillstyle(solidfill,cob);
                        poly[1]:=x1;
                        fillpoly(3,poly);
                    end
                """
        expect = str(Program([FuncDecl(Id('afficherfleche'),
                    [VarDecl(Id('x1'),IntType()),VarDecl(Id('x2'),IntType()),
                    VarDecl(Id('y1'),IntType()),VarDecl(Id('y2'),IntType()),
                    VarDecl(Id('allume'),BoolType())],
                    [VarDecl(Id('cob'),FloatType()),
                    VarDecl(Id('poly'),ArrayType(1,3,IntType()))],
                    [If(Id('allume'),
                        [Assign(Id('cob'),IntLiteral(2))],
                        [Assign(Id('cob'),IntLiteral(1))]),
                    CallStmt(Id('setfillstyle'),[Id('solidfill'),Id('cob')]),
                    Assign(ArrayCell(Id('poly'),IntLiteral(1)),Id('x1')),
                    CallStmt(Id('fillpoly'),[IntLiteral(3),Id('poly')])]
                    )]))
        self.assertTrue(TestAST.test(input,expect,380))
    def test_cmplx_prog_21(self):
        input = """ procedure affichertexte(x,y:integer;cob,coc:real;s:string;grass:boolean);
                    var n:real;x1,lgC:integer;
                    begin
                        setFillStyle(solidfill,cob);
                        for n:=1 to length(s) do
                        begin
                            outtextXY(x1,y,s[N]);
                            lgc:=largeurtexte(s[N],gras);
                        end
                    end
                """
        expect = str(Program([FuncDecl(Id('affichertexte'),
                    [VarDecl(Id('x'),IntType()),VarDecl(Id('y'),IntType()),
                    VarDecl(Id('cob'),FloatType()),VarDecl(Id('coc'),FloatType()),
                    VarDecl(Id('s'),StringType()),VarDecl(Id('grass'),BoolType())],
                    [VarDecl(Id('n'),FloatType()),
                    VarDecl(Id('x1'),IntType()),
                    VarDecl(Id('lgC'),IntType())],
                    [CallStmt(Id('setFillStyle'),[Id('solidfill'),Id('cob')]),
                    For(Id('n'),IntLiteral(1),CallExpr(Id('length'),[Id('s')]),True,
                    [CallStmt(Id('outtextXY'),[Id('x1'),Id('y'),ArrayCell(Id('s'),Id('N'))]),
                    Assign(Id('lgc'),CallExpr(Id('largeurtexte'),[ArrayCell(Id('s'),Id('N')),Id('gras')]))])]
                    )]))
        self.assertTrue(TestAST.test(input,expect,381))
    def test_cmplx_prog_22(self):
        input = """ procedure main();
                    begin
                        printLN("hello");
                    end
                    var i: integer;
                """
        expect = str(Program([FuncDecl(Id('main'),
                    [],
                    [],
                    [CallStmt(Id('printLN'),[StringLiteral('hello')])]
                    ),VarDecl(Id('i'),IntType())]))
        self.assertTrue(TestAST.test(input,expect,382))
    def test_cmplx_prog_23(self):
        input = """ procedure main();
                    begin
                        if a=b then
                            if a+b mod 2 =0 then
                                println("foo\\n");
                            else
                                print();
                    end
                """
        expect = str(Program([FuncDecl(Id('main'),
                    [],
                    [],
                    [If(BinaryOp('=',Id('a'),Id('b')),
                        [If(BinaryOp('=',BinaryOp('+',Id('a'),BinaryOp('mod',Id('b'),IntLiteral(2))),IntLiteral(0)),
                            [CallStmt(Id('println'),[StringLiteral('foo\\n')])],
                            [CallStmt(Id('print'),[])])],
                        [])]
                    )]))
        self.assertTrue(TestAST.test(input,expect,383))
    def test_cmplx_prog_24(self):
        input = """ procedure main();
                    begin
                    end
                    function goo():real;begin end
                    procedure a();begin end
                """
        expect = str(Program([FuncDecl(Id('main'),
                    [],
                    [],
                    []
                    ),FuncDecl(Id('goo'),
                    [],
                    [],
                    [],
                    FloatType()),
                    FuncDecl(Id('a'),
                    [],
                    [],
                    [])]))
        self.assertTrue(TestAST.test(input,expect,384))
    def test_cmplx_prog_25(self):
        input = """ function foo(a:integer):integer;
                    begin
                        { Nothing here! }
                    end
                    procedure main();
                    var name: String;
                    begin
                        write("Please enter your name: ");
                        ReadLn(name);
                        WriteLn("Hello ",name);
                    end
                """
        expect = str(Program([FuncDecl(Id('foo'),
                    [VarDecl(Id('a'),IntType())],
                    [],
                    [],
                    IntType()),
                    FuncDecl(Id('main'),
                    [],
                    [VarDecl(Id('name'),StringType())],
                    [CallStmt(Id('write'),[StringLiteral('Please enter your name: ')]),
                    CallStmt(Id('ReadLn'),[Id('name')]),
                    CallStmt(Id('WriteLn'),[StringLiteral('Hello '),Id('name')])])]))
        self.assertTrue(TestAST.test(input,expect,385))
    def test_cmplx_prog_26(self):
        input = """ var i,j: integer;
                    var e: real;
                """
        expect = str(Program([VarDecl(Id('i'),IntType()),
                            VarDecl(Id('j'),IntType()),
                            VarDecl(Id('e'),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,386))
    def test_cmplx_prog_27(self):
        input = """ procedure print(int: integer; str: string);
                    var res: string;
                    begin
                        AssertType(res);
                        If TypeOf(res) = int then res := toString(res);
                        printLn(res);
                    end
                    procedure main();
                    begin
                        print("Long");
                    end
                """
        expect = str(Program([FuncDecl(Id('print'),
                    [VarDecl(Id('int'),IntType()),VarDecl(Id('str'),StringType())],
                    [VarDecl(Id('res'),StringType())],
                    [CallStmt(Id('AssertType'),[Id('res')]),
                    If(BinaryOp('=',CallExpr(Id('TypeOf'),[Id('res')]),Id('int')),
                       [Assign(Id('res'),CallExpr(Id('toString'),[Id('res')]))],
                       []),
                    CallStmt(Id('printLn'),[Id('res')])]),
                    FuncDecl(Id('main'),
                    [],
                    [],
                    [CallStmt(Id('print'),[StringLiteral('Long')])])]))
        self.assertTrue(TestAST.test(input,expect,387))
    def test_cmplx_prog_28(self):
        input = """ procedure main();
                    var name: String;
                    begin
                        write("Please enter your name: ");
                        ReadLn(name);
                        WriteLn("Hello ",name);
                    end
                """
        expect = str(Program([FuncDecl(Id('main'),
                    [],
                    [VarDecl(Id('name'),StringType())],
                    [CallStmt(Id('write'),[StringLiteral('Please enter your name: ')]),
                    CallStmt(Id('ReadLn'),[Id('name')]),
                    CallStmt(Id('WriteLn'),[StringLiteral('Hello '),Id('name')])])]))
        self.assertTrue(TestAST.test(input,expect,388))
    def test_cmplx_prog_29(self):
        input = """ procedure mark(ActualMark, PossibleMark: integer;Percentage:real);
                    begin { PassOrFailSystem }
                        WriteLn("Please type in student\\'s mark: ");
                        ReadLn(ActualMark);
                        WriteLn("Please type in total possible mark: ");
                        ReadLn(PossibleMark);
                        Percentage:=(ActualMark/PossibleMark)*100;
                        If Percentage>=50 Then
                            WriteLn("Pass");
                        Else WriteLn("Fail");
                    End
                """
        expect = str(Program([FuncDecl(Id('mark'),
                    [VarDecl(Id('ActualMark'),IntType()),VarDecl(Id('PossibleMark'),IntType()),
                    VarDecl(Id('Percentage'),FloatType())],
                    [],
                    [CallStmt(Id('WriteLn'),[StringLiteral('Please type in student\\\'s mark: ')]),
                    CallStmt(Id('ReadLn'),[Id('ActualMark')]),
                    CallStmt(Id('WriteLn'),[StringLiteral('Please type in total possible mark: ')]),
                    CallStmt(Id('ReadLn'),[Id('PossibleMark')]),
                    Assign(Id('Percentage'),BinaryOp('*',BinaryOp('/',Id('ActualMark'),Id('PossibleMark')),IntLiteral(100))),
                    If(BinaryOp('>=',Id('Percentage'),IntLiteral(50)),
                       [CallStmt(Id('WriteLn'),[StringLiteral('Pass')])],
                       [CallStmt(Id('WriteLn'),[StringLiteral('Fail')])])])]))
        self.assertTrue(TestAST.test(input,expect,389))
    def test_cmplx_prog_30(self):
        input = """ function gcd(a,b:integer):real;
                    var x:integer;
                    begin
                        if b=0 then gcd:=a;
                        else begin
                            x:=a;
                            while (x>=b) do
                            begin
                                x:=x-b;
                            end
                            gcd:=gcd(b,x);
                        end
                    end
                """
        expect = str(Program([FuncDecl(Id('gcd'),
                    [VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),],
                    [VarDecl(Id('x'),IntType())],
                    [If(BinaryOp('=',Id('b'),IntLiteral(0)),
                        [Assign(Id('gcd'),Id('a'))],
                        [Assign(Id('x'),Id('a')),
                        While(BinaryOp('>=',Id('x'),Id('b')),
                              [Assign(Id('x'),
                                      BinaryOp('-',Id('x'),Id('b')))]),
                        Assign(Id('gcd'),CallExpr(Id('gcd'),[Id('b'),Id('x')]))])],
                    FloatType())]))
        self.assertTrue(TestAST.test(input,expect,390))   
    def test_cmplx_prog_31(self):
        input = """ procedure main();
                    begin 
                        if a < 1 then a := b := 1;
                    end
                """
        expect = str(Program([FuncDecl(Id('main'),
                    [],
                    [],
                    [If(BinaryOp('<',Id('a'),IntLiteral(1)),
                        [Assign(Id('b'),IntLiteral(1)),Assign(Id('a'),Id('b'))],
                        [])]
                    )]))
        self.assertTrue(TestAST.test(input,expect,391))
    def test_cmplx_prog_32(self):
        input = """ procedure main();
                    var a: integer;
                    begin
                        a := 1; 
                        while (a < 10) do
                        begin
                            if a < 5 then continue;
                            print();
                            a := a + 1;
                        end
                    end
                """
        expect = str(Program([FuncDecl(Id('main'),
                    [],
                    [VarDecl(Id('a'),IntType())],
                    [Assign(Id('a'),IntLiteral(1)),
                    While(BinaryOp('<',Id('a'),IntLiteral(10)),
                          [If(BinaryOp('<',Id('a'),IntLiteral(5)),
                              [Continue()],
                              []),
                          CallStmt(Id('print'),[]),
                          Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral(1)))])]
                    )]))
        self.assertTrue(TestAST.test(input,expect,392))    
    def test_cmplx_prog_33(self):
        input = """ procedure Restore(Message: string; ReturnCode: integer);
                    begin
                        Write(Message);
                        if ReturnCode <> OK then
                            Msg1(Output,1,addr(SayCalRe(ReturnCode)));
                        else Msg0(Output,2);
                        Close(Input);
                        Close(Output);
                    end
                """
        expect = str(Program([FuncDecl(Id('Restore'),
                    [VarDecl(Id('Message'),StringType()),VarDecl(Id('ReturnCode'),IntType())],
                    [],
                    [CallStmt(Id('Write'),[Id('Message')]),
                    If(BinaryOp('<>',Id('ReturnCode'),Id('OK')),
                       [CallStmt(Id('Msg1'),[Id('Output'),IntLiteral(1),
                                             CallExpr(Id('addr'),[CallExpr(Id('SayCalRe'),[Id('ReturnCode')])])])],
                       [CallStmt(Id('Msg0'),[Id('Output'),IntLiteral(2)])]),
                    CallStmt(Id('Close'),[Id('Input')]),
                    CallStmt(Id('Close'),[Id('Output')])]
                    )]))
        self.assertTrue(TestAST.test(input,expect,393))
    def test_cmplx_prog_34(self):
        input = """ procedure main();
                    var RoundRealRate:integer;
                    begin
                        TermOut(Output);
                        TermIn(Input);
                        BeginTcpIp(ReturnCode);
                        If ReturnCode <> OK then begin
                            Msg1(Output,4,addr(SayCalRe(ReturnCode)));
                            return;
                        end
                    end
                """
        expect = str(Program([FuncDecl(Id('main'),
                    [],
                    [VarDecl(Id('RoundRealRate'),IntType())],
                    [CallStmt(Id('TermOut'),[Id('Output')]),
                    CallStmt(Id('TermIn'),[Id('Input')]),
                    CallStmt(Id('BeginTcpIp'),[Id('ReturnCode')]),
                    If(BinaryOp('<>',Id('ReturnCode'),Id('OK')),
                       [CallStmt(Id('Msg1'),[Id('Output'),IntLiteral(4),
                                             CallExpr(Id('addr'),[CallExpr(Id('SayCalRe'),[Id('ReturnCode')])])]),
                        Return()],
                       [])]
                    )]))
        self.assertTrue(TestAST.test(input,expect,394))
    def test_cmplx_prog_35(self):
        input = """ procedure main();
                    var RoundRealRate:integer;
                    begin
                        TermOut(Output);
                        TermIn(Input);
                        { Inform TCPIP which notifications will be handled by the program }
                        Handle(_DATADelivered,BUFFERspaceAVAILABLE,ReturnCode);
                        If ReturnCode <> OK then begin
                            Restore ("Handle: ",ReturnCode);
                            return;
                        end
                    end
                """
        expect = str(Program([FuncDecl(Id('main'),
                    [],
                    [VarDecl(Id('RoundRealRate'),IntType())],
                    [CallStmt(Id('TermOut'),[Id('Output')]),
                    CallStmt(Id('TermIn'),[Id('Input')]),
                    CallStmt(Id('Handle'),[Id('_DATADelivered'),Id('BUFFERspaceAVAILABLE'),Id('ReturnCode')]),
                    If(BinaryOp('<>',Id('ReturnCode'),Id('OK')),
                       [CallStmt(Id('Restore'),[StringLiteral('Handle: '),Id('ReturnCode')]),
                        Return()],
                       [])]
                    )]))
        self.assertTrue(TestAST.test(input,expect,395))
    def test_cmplx_prog_36(self):
        input = """ procedure main();
                    var RoundRealRate:integer;
                    begin
                        (* Prompt user for operation parameters *)
                        Msg0(Output,5);
                        ReadLn(Line);
                        If (Substr(Ltrim(Line),1,1)="s") then
                            SendFlag:=TRUE;
                        else
                            SendFlag:=FALSE;
                    end
                """
        expect = str(Program([FuncDecl(Id('main'),
                    [],
                    [VarDecl(Id('RoundRealRate'),IntType())],
                    [CallStmt(Id('Msg0'),[Id('Output'),IntLiteral(5)]),
                    CallStmt(Id('ReadLn'),[Id('Line')]),
                    If(BinaryOp('=',CallExpr(Id('Substr'),[CallExpr(Id('Ltrim'),[Id('Line')]),IntLiteral(1),IntLiteral(1)]),StringLiteral('s')),
                       [Assign(Id('SendFlag'),BooleanLiteral(True))],
                       [Assign(Id('SendFlag'),BooleanLiteral(False))])]
                    )]))
        self.assertTrue(TestAST.test(input,expect,396))
    def test_cmplx_prog_37(self):
        input = """ procedure main();
                    var RoundRealRate:integer;
                    begin
                        with ConnectionInfo: array[1 .. 2] of string; do
                            Connection:=UNSPECIFIEDconnection;
                        while(count<5) do begin
                            GetNextNote(Note,True,ReturnCode);
                            if ReturnCode <> OK then begin
                                restore("GetNextNote: ",ReturnCode);
                                return;
                            end
                        end
                    end
                """
        expect = str(Program([FuncDecl(Id('main'),
                    [],
                    [VarDecl(Id('RoundRealRate'),IntType())],
                    [With([VarDecl(Id('ConnectionInfo'),ArrayType(1,2,StringType()))],
                          [Assign(Id('Connection'),Id('UNSPECIFIEDconnection'))]),
                          While(BinaryOp('<',Id('count'),IntLiteral(5)),
                                [CallStmt(Id('GetNextNote'),[Id('Note'),BooleanLiteral(True),Id('ReturnCode')]),
                                If(BinaryOp('<>',Id('ReturnCode'),Id('OK')),
                                   [CallStmt(Id('restore'),[StringLiteral('GetNextNote: '),Id('ReturnCode')]),
                                   Return()],
                                   [])])]
                    )]))
        self.assertTrue(TestAST.test(input,expect,397))
    def test_cmplx_prog_38(self):
        input = """ procedure main();
                    begin
                        a := 1 + 2*3; 
                    end
                """
        expect = str(Program([FuncDecl(Id('main'),
                    [],
                    [],
                    [Assign(Id('a'),BinaryOp('+',IntLiteral(1),BinaryOp('*',IntLiteral(2),IntLiteral(3))))]
                    )]))
        self.assertTrue(TestAST.test(input,expect,398))
    def test_cmplx_prog_39(self):
        input = """ procedure main();
                    begin
                        foo(true,1.e-8);
                    end
                """
        expect = str(Program([FuncDecl(Id('main'),
                    [],
                    [],
                    [CallStmt(Id('foo'),[BooleanLiteral(True),FloatLiteral(1.e-8)])]
                    )]))
        self.assertTrue(TestAST.test(input,expect,399))
    def test_cmplx_prog_40(self):
        input = """ procedure main();
                    begin
                        foo(true,1.e8);
                    end
                    procedure goo();
                    begin
                        while foo() do print();
                    end
                """
        expect = str(Program([FuncDecl(Id('main'),
                    [],
                    [],
                    [CallStmt(Id('foo'),[BooleanLiteral(True),FloatLiteral(1.e8)])]
                    ),FuncDecl(Id('goo'),
                    [],
                    [],
                    [While(CallExpr(Id('foo'),[]),
                    [CallStmt(Id('print'),[])])])]))
        self.assertTrue(TestAST.test(input,expect,400))
