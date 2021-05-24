using System;
using System.Collections.Generic;

namespace TecanSparkRelay.Protocols
{
    public class Plate
    {
        public int rows;
        public int columns;
        public List<Well> layout = new List<Well>();

        private char[] letters = "ABCDEFGHIJKLMNOPQRSTUVYWXYZ".ToCharArray();

        public Plate(int rows, int columns, int selectedWells)
        {
            if (rows > letters.Length)
            {
                throw new ApplicationException("number of rows cannot be more than 26");
            }

            this.rows = rows;
            this.columns = columns;

            // Build the plate layout
            for (int row = 0; row < rows; row++)
            {
                for (int col = 0; col < columns; col++)
                {
                    // Row-first indexing for the well index as per the method XML format
                    var index = col + (columns * row);

                    // Column-first indexing for selecting wells as per the conventions for well-based protocols
                    var selected = row + (rows * col) < selectedWells ? "True" : "False";

                    this.layout.Add(new Well
                    {
                        index = index,
                        row = row,
                        column = col,
                        selected = selected,
                        coordinate = $"{letters[row]}{col + 1}",
                    });
                }
            }
        }
    }

    public class Well
    {
        public int index;
        public int row;
        public int column;
        public string selected;
        public string coordinate;
    }
}
