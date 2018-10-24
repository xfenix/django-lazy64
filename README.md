Django search (or seo) hide
==

Let's see: what is this?
---

This is django search hide package

What for?
---

To hide links/content/whole site part from search indexation. REALLY hide. To reduce outer link page search engine weight (it leaks through external links) and increase page search engine weight.

Really hide?
---
Yeah. Noindex/nofollow/sitemaps/robots.txt can be ignored by various search engines across the world.
Sometimes you want to hide something on you site really bad. So, you can use this package to do it.

How is it working?
---
Really simple: template tags wraps around you content and turns it into base64 text, saved in javascript variable (global variable). Also, at the end of you template, you need to use another template tag, that outputs simple inlined and very small javascript, that grab those global variables, decode base64 from them and just place it into the DOM.
This is not a fast working solution (because DOM manipulations are slow), and if you use it against you menu, header or another big, top parts of you site, you can get the "kangaroo" effect, when you site just jumping in the each site reload.
So, i beg you - do not use it for so. Just hide small, but vital parts.

Usage
---
1. Import tag library `{% load searchhide %}`
2. Wrap desired html block in tags like this `{% do_shide %}HTML code{% enddo_shide %}`
3. Add `{% post_shide %}` tag call in the end of you html layout (before </body>)

Caching
---
I strongly reccomend you to use cache tags and wrap with them each of this tags.
