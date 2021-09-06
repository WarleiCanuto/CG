
void setup()
{
  size(800,800);
}

void draw()
{
  background(0, 20, 79);
  float p0x = 100;
  float p0y = 100;
  float p1x = 100;
  float p1y = 700;
  float p2x = 700;
  float p2y = 100;
  if(mousePressed && (mouseButton == LEFT)){
     p1x = mouseX;
     p1y = mouseY;
  } else if (mousePressed && (mouseButton == RIGHT)) {
     p2x = mouseX;
     p2y = mouseY;
  }
  float p3x = 700;
  float p3y = 700;
  fill(0);
  beginShape();
  vertex(p0x, p0y);
  for(float t = 0; t <= 1; t += 0.01)
  {

    float a0x = p0x + t*(p1x-p0x);
    float a0y = p0y + t*(p1y-p0y);

    float b0x = p1x + t*(p2x-p1x);
    float b0y = p1y + t*(p2y-p1y); 

    float a1x = p1x + t*(p2x-p1x);
    float a1y = p1y + t*(p2y-p1y);
    
    float b1x = p2x + t*(p3x-p2x);
    float b1y = p2y + t*(p3y-p2y);

    float ax = a0x + t*(b0x-a0x);
    float ay = a0y + t*(b0y-a0y);
    float bx = b0x + t*(b1x-b0x);
    float by = b0y + t*(b1y-b0y);

    float cx = ax + t*(bx-ax);
    float cy = ay + t*(by-ay);

    vertex(cx,cy);  
  }
  vertex(p3x, p3y);
  endShape(CLOSE);
}
