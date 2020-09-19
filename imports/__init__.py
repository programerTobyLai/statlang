import sys,os
ErrorStop=True
import platform
license_text="""MIT License

Copyright (c) 2020 Toby(tobylai,tobylaiApps,Toby)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
def exitprogram():
	if(ErrorStop):sys.exit(1)
	else:pass
class StatlangCore(object):
	"""Core"""
	def __init__(self):
		super( StatlangCore, self).__init__()
		self.funcs={}
		self.Line=0
		
	def new_func(self, name):
		def wraps(f):
			self.add_func(func=f, usename=name)
			return f

		return wraps

	def add_func(self,func,usename):
		self.funcs[usename]=func

	def runcode(self,code):
		'''
		p:hi
		'''
		lines=code.split('\n')
		self.Line=0
		for c in lines:
			self.Line+=1
			if(c):
				fa=c.split(':')
				if(len(fa)==1):throw_error('SyntaxError',f'Do you mean {fa[0]}: ?')
				if(self.funcs.get(fa[0].strip())):
					if(len(fa)>1):
						args_=':'.join(fa[1:]).split('|')
						args=[]
						for i in args_:
							if(i):args.append(f"'{i}',")
						# print(args)
						# print('self.funcs[fa[0]]({})'.format(''.join(args)))
						if(self.funcs[fa[0].strip()].__code__.co_argcount<len(args)):
							throw_error('ArgumentsError', f'"{fa[0].strip()}:" only takes {self.funcs[fa[0].strip()].__code__.co_argcount} positional argument but {len(args)} were given')
						# print('a',''.join(args))
						exec('self.funcs[fa[0].strip()]({})'.format(''.join(args)))
				else:
					throw_error('FuncNotFoundError',f'No function called "{fa[0].strip()}"')
						


core=StatlangCore()
@core.new_func('output')
def output(value='',):
	print(value)

@core.new_func('throw_error')
def throw_error(errorname,errorcontent):
	print(f"[{errorname}] {errorcontent} (on line {core.Line})")
	exitprogram()

@core.new_func('license')
def license():
	output(license_text)

@core.new_func('info')
def info():
	msg=f'''Statlang v0.1.2[beta],by Toby(tobylai) 
tip:if you wan to run a statlang file(.statlng),use "statlang --run <name>.statlng"
Running on {platform.system()} {platform.version()}
Type "license:" to get the license info.'''
	output(msg)