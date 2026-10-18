# Replaces $$...$$ formulas on pages with `math: true` by the SVGs that
# tools/render_maths.py typeset with LaTeX (IBM Plex Mono Italic) into _maths/.
# A formula on a line of its own is set as display maths, aligned to the right.
require "digest"
require "cgi"

module ICMNSMaths
  DISPLAY = /^[ \t]*\$\$(.+?)\$\$[ \t]*$/
  INLINE = /\$\$(.+?)\$\$/m

  def self.key(mode, tex)
    Digest::SHA1.hexdigest("#{mode}:#{tex.strip}")[0, 16]  # same as tools/render_maths.py
  end

  def self.svg(site, mode, tex, where)
    path = File.join(site.source, "_maths", "#{key(mode, tex)}.svg")
    label = CGI.escapeHTML(tex.strip)
    if File.exist?(path)
      %(<span class="math math-#{mode}" role="img" aria-label="#{label}">#{File.read(path).strip}</span>)
    else
      Jekyll.logger.warn "Maths:", "not typeset yet in #{where}: #{tex.strip} (run python3 tools/render_maths.py)"
      %(<code class="math-missing">#{label}</code>)
    end
  end

  def self.render(doc)
    return unless doc.data["math"]
    site = doc.site
    where = doc.relative_path
    doc.content = doc.content
      .gsub(DISPLAY) { "\n<div class=\"math-block\">#{svg(site, 'display', Regexp.last_match(1), where)}</div>\n" }
      .gsub(INLINE) { svg(site, "inline", Regexp.last_match(1), where) }
  end
end

Jekyll::Hooks.register [:pages, :documents], :pre_render do |doc|
  ICMNSMaths.render(doc)
end
