/**
 * Blog entry helpers.
 */

'use strict';

function build_footnotes() {
    var footnotes = $('div.footnote ol li')
    if (footnotes.length > 0) {
        footnotes.each(function(idx) {
            // Copy the entire footnote.
            var note = $(this).clone();
            // Find the 'jump back' link.
            var backlink = note.find('a.footnote-backref');
            if (backlink.length === 1) {
                // Grab the anchor by ID.
                var link = $(backlink.attr('href'));
                if (link.length === 1) {
                    // Whack the backlink, create the tool tip and prevent the default click action.
                    backlink.remove()
                    link.tooltip({
                        html: true,
                        title: note.html()
                    });
                    link.click(function(event) {
                        event.preventDefault();
                    });
                }
            }
        })
    }
}

$(document).ready(function() {
    build_footnotes();
});
