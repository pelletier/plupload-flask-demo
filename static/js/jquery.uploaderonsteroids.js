

function usteroids_generate_id() {
    /* You can call a webserver or whatever but return a string containing
     * a unique identifier for the current upload. */
    
    var uuid = "";
    for (i = 0; i < 32; i++) { uuid += Math.floor(Math.random() * 16).toString(16); }
    return uuid;
}

(function($){

$.fn.uploader(options) {
    
    var defaults = {
        generate_id: usteroids_generate_id
    };

    /* Override the defaults. */
    options = $.extend(defaults, options);

    return this.each(function(){
        $(this).bind('submit', function(){
        
            for (var i=0; i < this.files.length; i++) {
                
                var file = this.files[i];

                /* Create a form for each file to upload */
                var new_form = window.document.createElement('form');
                new.

            }

        });
    });

};

})(jQuery);
