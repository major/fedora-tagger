<li id="tag-${str(w.tag.id)}">
<div class="voter">
  <div class="arrow up" onclick="upvote(${str(w.tag.id)});"></div>
  <div class="total">${str(w.tag.total)}</div>
  <div class="arrow down" onclick="downvote(${str(w.tag.id)});"></div>
</div>
<a href="#">${w.tag.label.label}</a>
<div class="other_packages">${str(len(w.tag.label.packages)-1)} other packages.</div>
</li>