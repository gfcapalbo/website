

odoo.define('website_snippet_blog_display_post.snippet_editor', function(require) {
    "use strict";

    var options = require("web_editor.snippets.options");

    return options.registry.dispBlogOptions = options.Class.extend({
        select_value: function (event, value)
        {if (event == 'click') {
               var selection = value.split("_");
               var content = this.$target; 
               content.attr('data-parameter_id', selection[0])
                   .attr('data-blog_id', selection[1]);
            }
        },
        start: function()
        {   
            this.$target.find('.parametricTemplate').html("click here to select blog from options");
        },
        onFocus: function()
        {  
            this.$target.find('.parametricTemplate').html("Select blog to display from options");
        },
        clean_for_save: function() 
        {
            this.$target.find('.parametricTemplate')
                .empty()
                .append(
                    jQuery('<t />')
                    .attr('t-call', 'website_snippet_blog_display_post.blog_postcontent')
                    .attr('t-ignore-branding', '1')
                    .append(
                        jQuery('<t />')
                        .attr('t-value', this.$target.attr('data-blog_id'))
                        .attr('t-set', 'blog_id')
                        .attr('t-ignore-branding', '1'),
                        jQuery('<t />')
                        .attr('t-value', this.$target.attr('data-parameter_id'))
                        .attr('t-set', 'parameter_id')
                        .attr('t-ignore-branding', '1')
                    )
                );
        }

    });

});

