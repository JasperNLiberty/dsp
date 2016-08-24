# Choose and learn your editor(s)


Computing's interface is text. To work effectively, you need to be fluent with this interface.


### Typing

It may sound silly, but [make sure](http://www.typingtest.com/) you know how to type. You should be comfortable typing with perfect accuracy at 60 words per minute, at least. If you currently can't, practice until you can.

A lot of your work will be done in a text editor. You have to know how to use your editor. Any editor will work, but knowing a powerful editor well will make you faster, more comfortable, and more effective.

---

### Terminal Editor

Sometimes you will need to use a non-graphical text editor. This means an editor that will run entirely inside a terminal window, without spawning a new window, entirely without mouse input.

Make sure that you know at least one of these well enough to do basic editing in a terminal:

 * Emacs
 * vim
 * nano

You should know at least enough vim to be able to get out of it, because it is the default on many systems and you might find yourself in it even if you didn't mean to be.

If you intend to use a graphical editor that doesn't run in a terminal, nano might be a good choice for you because it is very simple.

Both Emacs and vim have built-in interactive tutorials that you can try.



---

###Graphical Editor

You will probably spend most of your time with access to a graphical interface, where you have more choices in editors and integrated development environments.

Popular editors and IDEs include:

 * Emacs
 * vim
 * Sublime
 * Atom
 * Spyder
 * PyCharm
 * [Rodeo](http://blog.yhat.com/posts/introducing-rodeo.html)

If you choose Emacs or vim, you will have essentially the same editor experience across graphical and non-graphical environments, which is nice. It's also nice to be able to work without ever having to use a mouse. Emacs and vim have somewhat steep learning curves, but they give you the ability to customize your environment quite a lot to make it exactly what you want.

Sublime is probably the most popular editor for new coders. You can set it up to integrate with Python fairly well. Atom is pretty similar to Sublime but has an interesting open architecture and is developed by folks at GitHub.

Spyder and PyCharm are IDEs for Python. They try to give you a fully configured setup out of the box.

We will also use Jupyter (IPython) notebooks, but this does not remove the need for proficiency in an editor or IDE.

---

###Q1. Terminal Editor

What terminal editor will you use? How did you make your decision?

>>You simply type vim into the terminal to open it and start a new file.

You can pass a filename as an option and it will open that file, e.g. vim main.c. You can open multiple files by passing multiple file arguments.

Vim has different modes, unlike most editors you have probably used. You begin in NORMAL mode, which is where you will spend most of your time once you become familiar with vim.

To return to NORMAL mode after changing to a different mode, press Esc. It's a good idea to map your Caps Lock key to Esc, as it's closer and nobody really uses the Caps Lock key.

The first mode to try is INSERT mode, which is entered with a for append after cursor, or i for insert before cursor.

To enter VISUAL mode, where you can select text, use v. There are many other variants of this mode, which you will discover as you learn more about vim.

To save your file, ensure you're in NORMAL mode and then enter the command :w. When you press :, you will see your command appear in the bottom status bar. To save and exit, use :x. To quit without saving, use :q. If you had made a change you wanted to discard, use :q!.

--

###Q2. Graphical Editor

What graphical editor will you use? How did you make your decision? What are some interesting features of your editor? What are some useful keyboard shortcuts for your editor? How do you customize your editor?

>> Atom

It integrates well with git.
It provides many customization options.
