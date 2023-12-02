# change color of diff text

## color.diff.\<slot>
Use customized color for diff colorization.  
\<slot> specifies which part of the patch to use the specified color, and is one of  
- context (context text - plain is a historical synonym),  
- meta (metainformation), frag (hunk header),  
- func (function in hunk header), 
- old (removed lines), 
- new (added lines), 
- commit (commit headers), 
- whitespace (highlighting whitespace errors), 
- oldMoved (deleted lines), 
- newMoved (added lines), 
 -oldMovedDimmed, 
 - oldMovedAlternative, 
 - oldMovedAlternativeDimmed, 
 - newMovedDimmed, 
 - newMovedAlternative newMovedAlternativeDimmed 
 (See the <mode> setting of --color-moved in git-diff[1] for details), contextDimmed, oldDimmed, newDimmed, contextBold, oldBold, and newBold (see git-range-diff[1] for details).

 ## example suitable for colorblind
```
git config --global color.diff.new blue
git config --global color.diff.old black

```
