#! /usr/bin/env python

# import stuff here

class Applicant(object):
    """ Docstring goes here """

    def __init__(self, position, name="John Doe"):
        self.raw_name = name
        self.position = position
        self.interviewed = False
        self.hired = False

    def name(self, style="long", printed=False):
        """
            The applicant returns his/her name formated as requested and
            optionally mirrored to stdout
        """
        if style.lower() == "short":
            display_name = self.raw_name.split()[0]
        elif style.lower() == "loud":
            display_name = self.raw_name.upper()
        else:
            display_name = self.raw_name

	if printed:
            print("Hi, my name is {}.".format(display_name))

        return display_name

    def interview(self):
        """ The applicant gets interviewed """
        self.interviewed = True
        return

    def hire(self):
        """ If the applicant has already been interviewed, hire him/her """
        if self.hired:
	    print("{} has already been hired.".format(self.name, "short"))
	elif self.interviewed:
            self.hired = True
	else:
            print("{} needs to be interviewed first!".format(self.name()))

        return self.hired


def main():
    """ This is how you hire Jake """
    applicant = Applicant("Cluster Boy", "Jacob Gotberg")
    applicant.name(printed=True)
    applicant.name("loud", printed=True)
    applicant.hire()  # opps
    applicant.interview()
    if applicant.hire():
        print("Congrats! You hired {} as a {}!".format(applicant.name("short"),
                                                       applicant.position))

if __name__ == "__main__":
    main()

