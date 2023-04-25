using System;
using System.Collections.Generic;
using System.Drawing;

namespace LR5
{
    struct Vector
    {
        public Vector(KeyValuePair<PointF, PointF> a)
        {
            A = a.Key.X - a.Value.X;
            B = a.Key.Y - a.Value.Y;
        }
        public Vector(float Vx, float Vy)
        {
            this.A = Vx;
            this.B = Vy;
        }
        public Vector(PointF begin, PointF end)
        {
            A = begin.X - end.X;
            B = begin.Y - end.Y;
        }
        public float A;
        public float B;
    }
    struct forSutherlandCohen
    {
        public forSutherlandCohen(Point min, Point max)
        {
            minPoint = min;
            pMax = max;
        }
        public forSutherlandCohen(float x_min, float y_min, float x_max, float y_max)
        {
            minPoint = new PointF(x_min, y_min);
            pMax = new PointF(x_max, y_max);
        }
        public PointF minPoint;
        public PointF pMax;
    }
    class Algorithms
    {
       public void SetRectangleClipper(float x_min, float y_min, float x_max, float y_max)
        {
            rect = new forSutherlandCohen(x_min, y_min, x_max, y_max);
        }
        public void SetRectangleClipper(Point min, Point max)
        {
            rect = new forSutherlandCohen(min, max);
        }
        
        public string getCode(PointF a)
        {
            string code = "";
            code += (a.Y > rect.pMax.Y ? '1' : '0');
            code += (a.Y < rect.minPoint.Y ? '1' : '0');
            code += (a.X > rect.pMax.X ? '1' : '0');
            code += (a.X < rect.minPoint.X ? '1' : '0');
            return code;
        }
        public PointF moveBit(PointF a, float k)
        {
            var code = getCode(a);
            if (code[2] == '1')
            {
                return new PointF(rect.pMax.X, a.Y + k * (rect.pMax.X - a.X));
            }
            if (code[3] == '1')
            {
                return new PointF(rect.minPoint.X, a.Y + k * (rect.minPoint.X - a.X));
            }
            if (code[0] == '1')
            {
                return new PointF(a.X + (1 / k) * (rect.pMax.Y - a.Y), rect.pMax.Y);
            }
            if (code[1] == '1')
            {
                return new PointF(a.X + (1 / k) * (rect.minPoint.Y - a.Y), rect.minPoint.Y);
            }
            return a;
        }
       public bool SutherlandCohen(PointF a, PointF b, ref PointF p1, ref PointF p2)
       {
            return true;
       }
        private void Swap(ref PointF a, ref PointF b)
        {
            PointF temp = a;
            a = b;
            b = temp;
        }
        public forSutherlandCohen rect;
        public List<Vector> vectors;
        public List<KeyValuePair<PointF, PointF>> edges;
        public float ScalarMultiply(Vector vec1, Vector vec2)
        {
            return (vec1.A * vec2.A + vec1.B * vec2.B);
        }

        public float VectorMultiply(Vector vec1, Vector vec2)
        {
            return vec1.A * vec2.B - vec1.B * vec2.A;
        }
        public void SetPolygon(List<KeyValuePair<PointF, PointF>> list)
        {
            vectors = new List<Vector>();
            edges = new List<KeyValuePair<PointF, PointF>>(list);
            for (int i = 0; i < list.Count; i++)
            {
                vectors.Add(new Vector(list[i].Key, list[i].Value));
            }

        }

        
        public float getParameter(PointF p, KeyValuePair<PointF, PointF> segment)
        {
            return (p.X - segment.Key.X) / (segment.Value.X - segment.Key.X);
        }
        public float getT(KeyValuePair<PointF, PointF> sides, KeyValuePair<PointF, PointF> segment, ref bool onSameLine)
        {
            var x0e = sides.Key.X;
            var y0e = sides.Key.Y;
            var x1e = sides.Value.X;
            var y1e = sides.Value.Y;


            var x0s = segment.Key.X;
            var y0s = segment.Key.Y;
            var x1s = segment.Value.X;
            var y1s = segment.Value.Y;

            float ks = (y1s - y0s)/(x1s - x0s);
            float ke = (y1e - y0e) / (x1e - x0e);

            float bs = y0s - ks * x0s;
            float be = y0e - ke * x0e;

            var x = (be - bs) / (ks - ke);
            if ((x - x0e) / (x1e - x0e) <= 0 || (x - x0e) / (x1e - x0e) >= 1)
            {
                return -1;
            }
            var te = (x - x0s) / (x1s - x0s);
            if (float.IsNaN(te) && ke == ks && be == bs)
            {
                onSameLine = true;
            }
            return te;
        }
       public void CyrusBeck(PointF a, PointF b, ref float t_1, ref float t_2)
       {
            
       }
    }
}
