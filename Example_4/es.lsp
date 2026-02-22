(defun c:es ( / ss i ent vlaObj minPt maxPt file fn x y z)
  (vl-load-com)

  ;; Otvaranje fajla za upis
  (setq fn (strcat (getvar "DWGPREFIX") "vrhovi.txt"))
  (setq file (open fn "w"))

  ;; Selekt solid objekata
  (setq ss (ssget '((0 . "3DSOLID"))))
  (if ss
    (progn
      (setq i 0)
      (repeat (sslength ss)
        (setq ent (ssname ss i))
        (setq vlaObj (vlax-ename->vla-object ent))

        ;; Dobivanje bounding boxa
        (vla-GetBoundingBox vlaObj 'minPt 'maxPt)
        (setq minPt (vlax-safearray->list minPt))
        (setq maxPt (vlax-safearray->list maxPt))

        ;; Ispis 8 vrhova bounding boxa
(write-line (strcat "Solid" ) file) 
       (foreach pt
          (list
            (list (car minPt) (cadr minPt) (caddr minPt))
            (list (car maxPt) (cadr minPt) (caddr minPt))
            (list (car minPt) (cadr maxPt) (caddr minPt))
            (list (car minPt) (cadr minPt) (caddr maxPt))
            (list (car maxPt) (cadr maxPt) (caddr minPt))
            (list (car maxPt) (cadr minPt) (caddr maxPt))
            (list (car minPt) (cadr maxPt) (caddr maxPt))
            (list (car maxPt) (cadr maxPt) (caddr maxPt))
          )
          (setq x (rtos (car pt) 2 4)
                y (rtos (cadr pt) 2 4)
                z (rtos (caddr pt) 2 4))
          (write-line (strcat x "," y "," z) file)
        )

        
        (setq i (1+ i))
 

     )
      (princ (strcat "\nVrhovi su upisani u fajl: " fn))
    )
    (princ "\nNema selektiranih 3DSOLID objekata.")
  )

  (close file)
  (princ)
)
