#!/usr/bin/python
import unittest
import os

import numpy as np

import pymatgen

from pymatgen.io.cifio import CifParser, CifWriter
from pymatgen.io.vaspio import Poscar
from pymatgen.core.periodic_table import Element, Specie
from pymatgen.core.lattice import Lattice
from pymatgen.core.structure import Structure

test_dir = os.path.join(os.path.dirname(os.path.abspath(pymatgen.__file__)), '..', 'test_files')

class  CifIOTest(unittest.TestCase):

    def test_CifParser(self):
        parser = CifParser(os.path.join(test_dir, 'LiFePO4.cif'))
        for s in parser.get_structures(True):
            self.assertEqual(s.formula, "Li4 Fe4 P4 O16", "Incorrectly parsed cif.")

        #test for disordered structures
        parser = CifParser(os.path.join(test_dir, 'Li10GeP2S12.cif'))
        for s in parser.get_structures(True):
            self.assertEqual(s.formula, "Li20.2 Ge2.06 P3.94 S24", "Incorrectly parsed cif.")

    def test_CifWriter(self):
        filepath = os.path.join(test_dir, 'POSCAR')
        poscar = Poscar.from_file(filepath)
        writer = CifWriter(poscar.struct)
        expected_cif_str = """#\#CIF1.1
##########################################################################
#               Crystallographic Information Format file 
#               Produced by PyCifRW module
# 
#  This is a CIF file.  CIF has been adopted by the International
#  Union of Crystallography as the standard for data archiving and 
#  transmission.
#
#  For information on this file format, follow the CIF links at
#  http://www.iucr.org
##########################################################################

data_FePO4
_symmetry_space_group_name_H-M          'P 1'
_cell_length_a                          10.4117668699
_cell_length_b                          6.06717187997
_cell_length_c                          4.75948953998
_cell_angle_alpha                       90.0
_cell_angle_beta                        90.0
_cell_angle_gamma                       90.0
_chemical_name_systematic               'Generated by pymatgen'
_symmetry_Int_Tables_number             1
_chemical_formula_structural            FePO4
_chemical_formula_sum                   'Fe4 P4 O16'
_cell_volume                            300.65685512
_cell_formula_units_Z                   4
loop_
  _symmetry_equiv_pos_site_id
  _symmetry_equiv_pos_as_xyz
   1  'x, y, z'
 
loop_
  _atom_site_type_symbol
  _atom_site_label
  _atom_site_symmetry_multiplicity
  _atom_site_fract_x
  _atom_site_fract_y
  _atom_site_fract_z
  _atom_site_attached_hydrogens
  _atom_site_B_iso_or_equiv
  _atom_site_occupancy
   Fe  Fe1  1  0.218728  0.750000  0.474867  0  .  1
   Fe  Fe2  1  0.281272  0.250000  0.974867  0  .  1
   Fe  Fe3  1  0.718728  0.750000  0.025133  0  .  1
   Fe  Fe4  1  0.781272  0.250000  0.525133  0  .  1
   P  P5  1  0.094613  0.250000  0.418243  0  .  1
   P  P6  1  0.405387  0.750000  0.918243  0  .  1
   P  P7  1  0.594613  0.250000  0.081757  0  .  1
   P  P8  1  0.905387  0.750000  0.581757  0  .  1
   O  O9  1  0.043372  0.750000  0.707138  0  .  1
   O  O10  1  0.096642  0.250000  0.741320  0  .  1
   O  O11  1  0.165710  0.046072  0.285384  0  .  1
   O  O12  1  0.165710  0.453928  0.285384  0  .  1
   O  O13  1  0.334290  0.546072  0.785384  0  .  1
   O  O14  1  0.334290  0.953928  0.785384  0  .  1
   O  O15  1  0.403358  0.750000  0.241320  0  .  1
   O  O16  1  0.456628  0.250000  0.207138  0  .  1
   O  O17  1  0.543372  0.750000  0.792862  0  .  1
   O  O18  1  0.596642  0.250000  0.758680  0  .  1
   O  O19  1  0.665710  0.046072  0.214616  0  .  1
   O  O20  1  0.665710  0.453928  0.214616  0  .  1
   O  O21  1  0.834290  0.546072  0.714616  0  .  1
   O  O22  1  0.834290  0.953928  0.714616  0  .  1
   O  O23  1  0.903358  0.750000  0.258680  0  .  1
   O  O24  1  0.956628  0.250000  0.292862  0  .  1
 
"""
        self.assertEqual(str(writer), expected_cif_str, "Incorrectly generated cif string")

    def test_disordered(self):
        si = Element("Si")
        n = Element("N")
        coords = list()
        coords.append(np.array([0, 0, 0]))
        coords.append(np.array([0.75, 0.5, 0.75]))
        lattice = Lattice(np.array([[ 3.8401979337, 0.00, 0.00], [1.9200989668, 3.3257101909, 0.00], [0.00, -2.2171384943, 3.1355090603]]))
        struct = Structure(lattice, [si, {si:0.5, n:0.5}], coords)
        writer = CifWriter(struct)
        ans = """#\#CIF1.1
##########################################################################
#               Crystallographic Information Format file 
#               Produced by PyCifRW module
# 
#  This is a CIF file.  CIF has been adopted by the International
#  Union of Crystallography as the standard for data archiving and 
#  transmission.
#
#  For information on this file format, follow the CIF links at
#  http://www.iucr.org
##########################################################################

data_Si1.5N0.5
_symmetry_space_group_name_H-M          'P 1'
_cell_length_a                          3.8401979337
_cell_length_b                          3.84019899434
_cell_length_c                          3.84019793372
_cell_angle_alpha                       119.999990864
_cell_angle_beta                        90.0
_cell_angle_gamma                       60.0000091373
_chemical_name_systematic               'Generated by pymatgen'
_symmetry_Int_Tables_number             1
_chemical_formula_structural            Si1.5N0.5
_chemical_formula_sum                   'Si1.5 N0.5'
_cell_volume                            40.0447946443
_cell_formula_units_Z                   1
loop_
  _symmetry_equiv_pos_site_id
  _symmetry_equiv_pos_as_xyz
   1  'x, y, z'
 
loop_
  _atom_site_type_symbol
  _atom_site_label
  _atom_site_symmetry_multiplicity
  _atom_site_fract_x
  _atom_site_fract_y
  _atom_site_fract_z
  _atom_site_attached_hydrogens
  _atom_site_B_iso_or_equiv
  _atom_site_occupancy
   Si  Si1  1  0.000000  0.000000  0.000000  0  .  1
   Si  Si2  1  0.750000  0.500000  0.750000  0  .  0.5
   N  N3  1  0.750000  0.500000  0.750000  0  .  0.5
 
"""
        self.assertEqual(str(writer).strip(), ans.strip())

    def test_specie_cifwriter(self):
        si4 = Specie("Si", 4)
        si3 = Specie("Si", 3)
        n = Specie("N", -3)
        coords = list()
        coords.append(np.array([0, 0, 0]))
        coords.append(np.array([0.75, 0.5, 0.75]))
        coords.append(np.array([0.5, 0.5, 0.5]))
        lattice = Lattice(np.array([[ 3.8401979337, 0.00, 0.00], [1.9200989668, 3.3257101909, 0.00], [0.00, -2.2171384943, 3.1355090603]]))
        struct = Structure(lattice, [si4, {si3:0.5, n:0.5}, n], coords)
        writer = CifWriter(struct)
        ans = """#\#CIF1.1
##########################################################################
#               Crystallographic Information Format file 
#               Produced by PyCifRW module
# 
#  This is a CIF file.  CIF has been adopted by the International
#  Union of Crystallography as the standard for data archiving and 
#  transmission.
#
#  For information on this file format, follow the CIF links at
#  http://www.iucr.org
##########################################################################

data_Si1.5N1.5
_symmetry_space_group_name_H-M          'P 1'
_cell_length_a                          3.8401979337
_cell_length_b                          3.84019899434
_cell_length_c                          3.84019793372
_cell_angle_alpha                       119.999990864
_cell_angle_beta                        90.0
_cell_angle_gamma                       60.0000091373
_chemical_name_systematic               'Generated by pymatgen'
_symmetry_Int_Tables_number             1
_chemical_formula_structural            Si1.5N1.5
_chemical_formula_sum                   'Si1.5 N1.5'
_cell_volume                            40.0447946443
_cell_formula_units_Z                   0
loop_
  _symmetry_equiv_pos_site_id
  _symmetry_equiv_pos_as_xyz
   1  'x, y, z'
 
loop_
  _atom_type_symbol
  _atom_type_oxidation_number
   Si4+  4
   N3-  -3
   Si3+  3
 
loop_
  _atom_site_type_symbol
  _atom_site_label
  _atom_site_symmetry_multiplicity
  _atom_site_fract_x
  _atom_site_fract_y
  _atom_site_fract_z
  _atom_site_attached_hydrogens
  _atom_site_B_iso_or_equiv
  _atom_site_occupancy
   Si4+  Si1  1  0.000000  0.000000  0.000000  0  .  1
   N3-  N2  1  0.750000  0.500000  0.750000  0  .  0.5
   Si3+  Si3  1  0.750000  0.500000  0.750000  0  .  0.5
   N3-  N4  1  0.500000  0.500000  0.500000  0  .  1
"""
        self.assertEqual(str(writer).strip(), ans.strip())

if __name__ == '__main__':
    unittest.main()

