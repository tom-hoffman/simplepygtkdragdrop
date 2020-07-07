Simplest Python GTK Drag and Drop Example
-----------------------------------------

Tom Hoffman
Computer Science Teacher
Providence Career and Technical Academy

In the course of figuring out how to implement drag and drop
in a GTK+ application I'm working on, I found I needed an even
simpler example than the ones I found on the web.

The really hard part with this is the lack of error messages if
you haven't wired up things properly.  One missing piece and
nothing happens (silently).

So I wrote this.  Bear in mind that I'm not an expert but I'm
taking a little extra time to make this a straightforward
and clean example.  

Basically you have a Drag button and a Drop button.
You drag the Drag button onto the Drop button and get some
signals printing info to the console hopefully illuminating
what is happening.  That's it.

You may not need all these signals to
get started in your app, I've included a few extras which may
be helpful in getting started and debugging your code.

This example will ONLY pass text; i.e., strings.  You can also
pass URI's, Pixbufs or Gdk.Atom's but that's outside my needs
or understanding at this point.  Limiting yourself to text
simplifies the process a lot.
